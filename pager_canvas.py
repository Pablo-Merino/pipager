from PIL import Image,ImageDraw,ImageFont

class Canvas:
  def __init__(self, epd):
    self.epd = epd
    self.canvas = Image.new('1', (self.epd.height, self.epd.width), 0xff)  # 212*104
    self.drawer = ImageDraw.Draw(self.canvas)

  def text(self, xy, text):
    self.drawer.text(xy, text, fill=0)

  def line(self, xy, width):
    self.drawer.line(xy, fill=0, width=1)

  def draw(self):
    buffer = self.epd.getbuffer(self.canvas)
    self.epd.pwndisplay(buffer)

  def clear(self):
    self.epd.pwnclear()
