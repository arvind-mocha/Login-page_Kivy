from kivy.animation import Animation
from kivy.uix.videoplayer import VideoPlayer

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.uix.video import Video
import pyodbc


#USER DEFINED
from string_validation import checkemail
from string_validation import checkpassword
from string_validation import checkname
from Date_and_Time import date
from Date_and_Time import time
from search import Binarysearch
from Database import singin_validator
import Database

#DATE AND TIME
t = time()
d = date()

#DATABASE
conn = pyodbc.connect(DSN='kivy_storage',autocommit=True)
cursor = conn.cursor()
data=Database

#FONTS
LabelBase.register(name='Black', fn_regular='kivymd/fonts/Roboto-Black.ttf')
LabelBase.register(name='Chausson', fn_regular='FONTS\chausson\ChaussonCFBold-Bold.otf')
LabelBase.register(name='Pacifico', fn_regular='FONTS\pacifico\Pacifico.ttf')
LabelBase.register(name='RMItalic', fn_regular='FONTS/raleway/Raleway-MediumItalic.ttf')
LabelBase.register(name='AR', fn_regular='FONTS/amatic/AmaticSC-Regular.ttf')
LabelBase.register(name='FFF', fn_regular="FONTS\FFF\FFF_Tusj.ttf")

#LOADING FILE
kv = Builder.load_file('login.kv')



#SCREENS
class Singup_or_Singin(Screen):
     pass

class Singup(Screen):
    s2_user_name_in = ObjectProperty()
    s2_email_in = ObjectProperty()
    s2_password_in = ObjectProperty()

    def s2name_checker(self):
        if Binarysearch(data.name_validation,0,len(data.name_validation)-1,self.s2_user_name_in.text) !='valid' and self.s2_user_name_in.text != "":
            validation = 'valid'
        else:
            validation = 'invalid'
            self.s2_user_name_in.text = ""
            print('username already exist')
        return validation


    def s2email_checker(self):
        if Binarysearch(data.email_validation,0,len(data.email_validation)-1,self.s2_email_in.text)!='valid' and self.s2_email_in.text != "":
            validation = 'valid'
        else:
            validation = 'invalid'
            self.s2_email_in.text = ""
            print("email already exist")
        return validation


    def s2DbStorage(self):
        if checkname(self.s2_user_name_in.text) == 'valid':
            if checkemail(self.s2_email_in.text) == 'valid':
                if checkpassword(self.s2_password_in.text) == 'valid':
                    try:
                        cursor.execute("insert into singup(userid,username,email,password,date_of_creation,time_of_creation)"
                                        "values(?,?,?,?,?,?)",f'{data.uid}',f'{self.s2_user_name_in.text}',
                                        f'{self.s2_email_in.text}',f'{self.s2_password_in.text}',f'{d}', f'{t}')
                    except pyodbc.IntegrityError:
                        pass
                    print('valid and info stored')
                    return 'valid'
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

    def s3user_checker(self):
        if singin_validator(self.s3_user_name_in.text,self.s3_password_in.text) != 'invalid':
            validation = singin_validator(self.s3_user_name_in.text,self.s3_password_in.text)
        else:
            validation = 'invalid'
        return validation


    def s3DbStorage(self):
        try:
            if checkname(self.s3_user_name_in.text) == 'valid':
                if checkpassword(self.s3_password_in.text) == 'valid':
                    cursor.execute("insert into singin(userid,logged_in_as,time_of_login,date_of_login) values(?,?,?,?)",
                                     f'{self.s3user_checker()}',f'{self.s3_user_name_in.text}', f'{t}',f'{d}')

                    print('authentication complete')
                    return 'valid'
                else:
                    print('invalid password')
                    self.s3_password_in.text = ""
            else:
                print('invalid name')
                self.s3_user_name_in.text = ""
        except :
            pass

    def s3textclear(self):
        self.s3_user_name_in.text = ""
        self.s3_password_in.text = ""


class Done(Screen):
    pass

class home(Screen):
    manager = ObjectProperty()
    data = {'icons/food.ico':'food',
            'icons/traveling.ico':'traveling',
            'icons/shopping.ico':'shopping',
            'icons/movie.ico':'movie'}

    def callback(self, instance):
        if instance.icon == 'icons/movie.ico':
            self.manager.transition.direction = 'right'
            self.manager.transition.duration =0.4
            self.manager.current = 'movie'
            print('movie button pressed')
        elif instance.icon == 'icons/shopping.ico':
            self.manager.transition.direction = 'right'
            self.manager.transition.duration = 0.4
            self.manager.current = 'shopping'
            print('online shopping button pressed')
        elif instance.icon == 'icons/traveling.ico':
            self.manager.transition.direction = 'right'
            self.manager.transition.duration = 0.4
            self.manager.current = 'travel'
            print('traveling pressed')
        elif instance.icon == 'icons/food.ico':
            self.manager.transition.direction = 'right'
            self.manager.transition.duration = 0.4
            self.manager.current = 'food'
            print('food button pressed')

class movie(Screen):
    pass

class shopping(Screen):
    pass

class food(Screen):
    pass

class travel(Screen):
    pass

class WindowManager(ScreenManager):
    pass


#APP
class Myapp(MDApp):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    Myapp().run()