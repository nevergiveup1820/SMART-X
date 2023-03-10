from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import webbrowser
import cv2
from kivymd.uix.screen import Screen

Window.size = (400, 600)

navigation_helper = """
Screen:
    name: "MainScreen"
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Smart I"
            md_bg_color: .2,.2,.2,1
            specific_text_color: 1,1,1,1


        MDBottomNavigation:

            MDBottomNavigationItem:
                name: "HomeScreen"
                icon: 'home'
                text: "Home"

                MDLabel:
                    text:"Other my projects"
                    pos_hint:{"center_x":.5,"center_y":.93}
                    halign:"center"
                    theme_text_color:"Custom"
                    text_color: "white"
                    font_size:"20sp"

                BoxLayout:
                    orientation: 'horizontal'
                    spacing: 15
                    pos_hint: {"center_x": .555,}

                    MDRaisedButton:
                        text:"Robot Smart-I"
                        font_size: 25

                        markup: True
                        pos_hint: {"center_x": .5, "center_y": .8}
                        md_bg_color:('5186C5')
                        text_color: "white"

                    MDRaisedButton:
                        text:"Car smart-e"
                        font_size:25
                        markup: True

                        pos_hint:{"center_y":.8}
                        md_bg_color:('5186C5')
                        text_color: "white"

                    # About

                MDLabel:
                    text:"About this App"
                    pos_hint:{"center_x":.5,"center_y":.63}
                    halign:"center"
                    theme_text_color:"Custom"
                    text_color: ('5186C5')
                    font_size:"28sp"

                MDLabel:
                    text:"This prog made “Garik Martirosyan” 3/19/2023 at age 14: This is his first program:"
                    pos_hint:{"center_x":.5,"center_y":.4}
                    halign:"center"
                    theme_text_color:"Custom"
                    text_color: "white"
                    font_size:"22sp"
                MDLabel:
                    text:"Made by Garik Martirosyan"
                    pos_hint:{"center_x":.5,"center_y":.2}
                    halign:"center"
                    theme_text_color:"Custom"
                    text_color: ('5186C5')
                    font_size:"22sp"

            MDBottomNavigationItem:
                name: "Camera"
                icon: 'home'
                text: "Camera"

                MDBoxLayout:
                    orientation: "vertical"


                    Camera:
                        id: camera

                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "48dp"

                        MDRectangleFlatButton:
                            text: "Start"
                            on_release: camera.play = True

                        MDRectangleFlatButton:
                            text: "Stop"
                            on_release: camera.play = False


            MDBottomNavigationItem:
                name: "TextEditor"
                icon: 'eyedropper'
                text: "TextEditor"

                MDLabel:
                    text: "TextEditor"
                    halign: 'center'
            MDBottomNavigationItem:
                name: "Links"
                icon: 'link'
                text: "Links"

                BoxLayout:
                    orientation: "vertical"
                    spacing: 24
                    pos: 0,root.height-(root.height*0.7)



                    MDRectangleFlatButton:
                        text: "Click here to open Google search"
                        pos_hint: {"center_x":.5}

                        font_size: "16sp"
                        markup: True
                        on_release: app.open_link("http://www.google.com")
                    MDRectangleFlatButton:
                        text: "Click here to open Youtube"
                        pos_hint: {"center_x":.5}

                        font_size: "16sp"
                        markup: True
                        on_release: app.open_link("https://www.youtube.com/")


                    MDRectangleFlatButton:
                        text: "Click here to open Instagram"
                        pos_hint: {"center_x":.5}

                        font_size: "16sp"
                        markup: True
                        on_release: app.open_link("http://www.google.com")


                    MDRectangleFlatButton:
                        text: "Click here to open Viber"
                        pos_hint: {"center_x":.5}

                        font_size: "16sp"
                        markup: True
                        on_release: app.open_link("http://www.google.com")



            MDBottomNavigationItem:
                name: "Voice"
                icon: 'link'
                text: "Assistant"

                MDLabel:
                    text: "Voice Assistant"
                    halign: 'center'
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.primary_palette = "BlueGray"

        return screen

    def open_link(self, link):
        webbrowser.open(link)


DemoApp().run()