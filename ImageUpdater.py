import Image, ImageFont, ImageOps, ImageDraw
import sys

class ImageUpdater():

    def __init__(self):
        self.my_font = ImageFont.truetype("Purisa-Bold.ttf", 50)

    def set_font_properties(self, font = "Purisa-Bold.ttf", size = 50):
        self.my_font = ImageFont.truetype(font, size)

    def create_text_image(self, text, size = (500,100), rotation = 0):
        self.text_image = Image.new('L', size)
        self.text_drawing = ImageDraw.Draw(self.text_image)
        self.text_drawing.text((0,0), text, font = self.my_font, fill = 255)
        self.text_image = self.text_image.rotate(rotation, expand = 1)

        return self.text_image

    def add_text_image(self, base, text, colour = (255,255,84), offset = (242,60)):
        base.paste(ImageOps.colorize(text, (0,0,0), colour), offset, text)

        return base

    def open_image(self, uri):
        try:
            return Image.open(uri)

        except IOError:
            raise IOError('Image does not exist')

    def save_image(self, image, uri):
        image.save(uri, 'PNG')
