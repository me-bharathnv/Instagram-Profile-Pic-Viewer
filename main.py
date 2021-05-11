from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from layout import window_helper
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from instaloader import Instaloader
from glob import glob


class insta(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.user = Builder.load_string(window_helper)
        button = MDRectangleFlatButton(text="Instagram Profile pic viewer",
                                       pos_hint={"center_x":0.5,"center_y":0.9} ,size_hint=(1,0.1))
        button_2 = MDRectangleFlatButton(text="view Image",pos_hint={"center_x":0.5,"center_y":0.6},
                    on_release = self.show_image )

        self.screen.add_widget(button_2)
        self.screen.add_widget(button)
        self.screen.add_widget(self.user)
        return self.screen

    def show_image(self,obj):
        instaloader = Instaloader()
        username = self.user.text
        instaloader.download_profile(username, profile_pic_only=True)
        filename = glob(str(username+"/*jpg"))
        img_data = str(filename[0])
        image = Image(source=img_data , pos_hint={"center_x": 0.5, "center_y": 0.3}, size_hint=(0.5, 1))
        image.remove_widget(image)
        self.screen.add_widget(image)

insta().run()