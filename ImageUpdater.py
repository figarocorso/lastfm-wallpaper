import Image, ImageFont, ImageOps, ImageDraw
import sys

class ImageUpdater():

    def __init__(self, base_image_uri):
        self.my_font = ImageFont.truetype("Purisa-Bold.ttf", 50)
        self.base = self.open_image(base_image_uri)
        self.colour = (255,255,84)

    def set_font_properties(self, font = "Purisa-Bold.ttf", size = 50, colour = (255,255,84)):
        self.my_font = ImageFont.truetype(font, size)
        self.colour = colour

    def create_text_image(self, text, size = (1000,300), rotation = 0):
        self.text_image = Image.new('L', size)
        self.text_drawing = ImageDraw.Draw(self.text_image)
        self.text_drawing.text((0,0), text, font = self.my_font, fill = 255)
        self.text_image = self.text_image.rotate(rotation, expand = 1)

        return self.text_image

    def add_text_image(self, text_image, offset = (242,60)):
        self.base.paste(ImageOps.colorize(text_image, (0,0,0), self.colour), offset, text_image)

        return self.base

    def add_username(self, username):
        self.set_font_properties(size = 30, colour = (30,30,30))
        self.username_image = self.create_text_image(username, rotation = 5)
        self.add_text_image(self.username_image, offset = (100,100))

    def add_scrobblings(self, scrobblings):
        self.set_font_properties(size = 30, colour = (30,30,30))
        self.scrobblings_string = str(scrobblings) + ' scrobblings are absolutely awesome'
        self.scrobblings_image = self.create_text_image(self.scrobblings_string, rotation = 5)
        self.add_text_image(self.scrobblings_image, offset = (100,140))

    def weekly_chart(self, artists):
        self.set_font_properties(size = 20, colour = (30,30,30))
        self.artist_image= self.create_text_image('Top chart:', rotation = -3)
        self.add_text_image(self.artist_image, offset = (150,290))
        for artist in artists:
            self.artist_string = str(artist[1]) + ' with ' + str(artist[2]) + ' tracks'
            self.artist_image= self.create_text_image(self.artist_string, rotation = -3)
            self.add_text_image(self.artist_image, offset = (150,330+40*artist[0]))


    def open_image(self, uri):
        try:
            return Image.open(uri)

        except IOError:
            raise IOError('Image does not exist')

    def get_base_image(self):
        return self.base

    def save_image(self, image, uri):
        image.save(uri, 'PNG')
