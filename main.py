from kivy.app import App
from kivy.uix.screenmanager import Screen
from os import system
from PIL import Image, ImageDraw, ImageFilter
import random
system('pip install Pillow')



class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_image(self,image):
        pass

    def load(self,image):
        self.ids.img.source = image

    def black_white(self,image):
        img = Image.open(image)
        BaW = img.convert("L")
        BaW.save(image+"black_white.png")
        self.ids.img.source = (image+"black_white.png")

    def inverse(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(image+"invert.png")
        self.ids.img.source = (image+"invert.png")

    def line_drawing(self,image):
        image = Image.open(image)
        image = image.convert("L")
        image = image.filter(ImageFilter.FIND_EDGES)

        image.save(r"lined.png")
        self.ids.img.source = ("lined.png")

    def pointillism(self,image):
        img = Image.open(image)
        pixels = img.load()
        width, height = img.size
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")

        for i in range(500000):
            size = random.randint(3, 5)
            x = random.randint(0, width - size)
            y = random.randint(0, height - size)

            ellipsebox = [(x, y), (x + size, y + size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
            del draw
        canvas.save(image+"pointillism.png")
        self.ids.img.source = (image+"pointillism.png")

    def sepia(self,image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]

                red = int(red * .393 + green * 0.769 + blue * 0.189)
                green = int(red * .349 + green * 0.686 + blue * 0.168)
                blue = int(red * .272 + green * 0.534 + blue * 0.131)
                pixels[x, y] = (red, green, blue)
        img.save(image+"sepia.png")
        self.ids.img.source = (image+"sepia.png")

images = ["lfa.jpg","blue_flower.jpg"]

PhotoGalleryApp().run()
