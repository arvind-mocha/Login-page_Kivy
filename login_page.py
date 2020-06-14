from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
import pyodbc

#USER DEFINED
from String_validation import checkemail
from String_validation import checkpassword
from String_validation import checkname
from Date_And_Time import date
from Date_And_Time import time
from random_value_generator import random_numbers

#DATE AND TIME
t = time()
d = date()

#FONTS
LabelBase.register(name='Black', fn_regular='E:/PROJECTS/GUI_kivy/kivymd/fonts/Roboto-Black.ttf')
LabelBase.register(name='Chausson', fn_regular='E:\PROJECTS\GUI_kivy\FONTS\chausson\ChaussonCFBold-Bold.otf')
LabelBase.register(name='Pacifico', fn_regular='E:\PROJECTS\GUI_kivy\FONTS\pacifico\Pacifico.ttf')
LabelBase.register(name='RMItalic', fn_regular='E:/PROJECTS/GUI_kivy/FONTS/raleway/Raleway-MediumItalic.ttf')
LabelBase.register(name='AR', fn_regular='E:/PROJECTS/GUI_kivy/FONTS/amatic/AmaticSC-Regular.ttf')
LabelBase.register(name='FFF', fn_regular="E:\PROJECTS\GUI_kivy\FONTS\FFF\FFF_Tusj.ttf")


#DATABASE CONNECTION
conn = pyodbc.connect(DSN='kivy_storage',autocommit=True)
cursor = conn.cursor()
singup_name_validation = [c[0] for c in cursor.execute('select username from singup')]
singup_email_validation = [e[0] for e in cursor.execute('select email from singup')]

#LOADING FILE
Builder.load_file('login.kv')


#SCREENS
class Singup_or_Singin(Screen):
     pass

class Singup(Screen):
    s2_user_name_in = ObjectProperty()
    s2_email_in = ObjectProperty()
    s2_password_in = ObjectProperty()

    def name_checker(self):
        for i in range(len(singup_email_validation)):
            if singup_name_validation[i] == self.s2_user_name_in.text:
                print('user name exist')
                validation = 'invalid '
                self.s2_user_name_in.text = ""
                break
            else:
                validation = 'valid'

        return validation

    def email_checker(self):
        for j in range(len(singup_email_validation)):
            if singup_email_validation[j] == self.s2_email_in.text:
                print('email already exist')
                validation = 'invalid '
                self.s2_email_in.text = ""
                break
            else:
                validation = 'valid'

        return validation



    def s2DbStorage(self):
        if checkname(self.s2_user_name_in.text) == 'valid':
            if checkemail(self.s2_email_in.text) == 'valid':
                if checkpassword(self.s2_password_in.text) == 'valid':
                    cursor.execute( "insert into singup(userid,username,email,password,date_of_creation,time_of_creation) "
                                    "values(?,?,?,?,?,?)",f'{random_numbers(99,200)}',f'{self.s2_user_name_in.text}',
                                    f'{self.s2_email_in.text}',f'{self.s2_password_in.text}',f'{d}', f'{t}')
                    print('valid and info stored')
                    self.s2_user_name_in.text = ""
                    self.s2_email_in.text = ""
                    self.s2_password_in.text = ""
                else:
                    print('invalid password')
                    self.s2_password_in.text = ""
            else:
                self.s2_email_in.text = ""
                print('invalid email ')
        else:
            self.s2_user_name_in.text = ""
            print('invalid name')

    def s2textclear(self):
        self.s2_user_name_in.text = ""
        self.s2_email_in.text = ""
        self.s2_password_in.text = ""

class Singin(Screen):
    s3_user_name_in = ObjectProperty()
    s3_password_in = ObjectProperty()

    def s3DbStorage(self):
        if checkname(self.s3_user_name_in.text) == 'valid':
            if checkpassword(self.s3_password_in.text) == 'valid':

                cursor.execute("insert into singin(logged_in_as,time_of_login,date_of_login) values(?,?,?)",
                                 f'{self.s3_user_name_in.text}', f'{t}',f'{d}')

                print('valid')
                self.s3_user_name_in.text = ""
                self.s3_password_in.text = ""
            else:
                print('invalid password')
                self.s3_password_in.text = ""
        else:
            print('invalid name')
            self.s3_user_name_in.text = ""

    def s3textclear(self):
        self.s3_user_name_in.text = ""
        self.s3_password_in.text = ""

class WindowManager(ScreenManager):
    pass


#APP
class Myapp(MDApp):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    Myapp().run()