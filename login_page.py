from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.text import LabelBase
#FONTS
LabelBase.register(name='Black', fn_regular='E:/PROJECTS/GUI/kivymd/fonts/Roboto-Black.ttf')
LabelBase.register(name='Chausson', fn_regular='E:\PROJECTS\GUI\FONTS\chausson\ChaussonCFBold-Bold.otf')
LabelBase.register(name='Pacifico', fn_regular='E:\PROJECTS\GUI\FONTS\pacifico\Pacifico.ttf')
LabelBase.register(name='RMItalic', fn_regular='E:/PROJECTS/GUI/FONTS/raleway/Raleway-MediumItalic.ttf')
LabelBase.register(name='AR', fn_regular='E:/PROJECTS/GUI/FONTS/amatic/AmaticSC-Regular.ttf')
LabelBase.register(name='FFF', fn_regular="E:\PROJECTS\GUI\FONTS\FFF\FFF_Tusj.ttf")


Builder.load_file('login.kv')

class Singup_or_Singin(Screen):
     pass

class Singup(Screen):
    s2_user_name_in = ObjectProperty()
    s2_email_in = ObjectProperty()
    s2_password_in = ObjectProperty()
    def s2textclear(self):
        self.s2_user_name_in.text=""
        self.s2_email_in.text=""
        self.s2_password_in.text=""

class Singin(Screen):
    s3_user_name_in = ObjectProperty()
    s3_password_in = ObjectProperty()
    def s3textclear(self):
        self.s3_user_name_in.text=""
        self.s3_password_in.text=""

class WindowManager(ScreenManager):
    pass



class Myapp(MDApp):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    Myapp().run()