from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build (self):
        return Button (text= "Hello world! This is my first program in kivy \n I'm a SESIANO student, and I love my teacher")
if __name__ == "__main__":
    MyApp().run()


