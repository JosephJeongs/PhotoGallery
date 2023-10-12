from kivy.app import App
from kivy.uix.screenmanager import Screen

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self,bool):
        if bool:
            return images[index]

    # def advance(self):
    #     global index, image
    #     if index<len(images):
    #         index += 1
    #     else:
    #         index = 0


images = ["white_lexus.jpg","blue_flower.jpg"]
index = 0

PhotoGalleryApp().run()
