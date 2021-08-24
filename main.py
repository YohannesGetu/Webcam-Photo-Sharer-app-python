from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

from filesharer import FileSharer

# fix opengl error
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
