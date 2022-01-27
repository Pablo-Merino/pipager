from PIL import Image,ImageDraw,ImageFont

class Canvas:
  def __init__(self, epd):
    self.epd = epd
    self.generate_canvas()

  def generate_canvas(self):
    self.canvas = Image.new('1', (self.epd.height, self.epd.width), 0xff)  # 212*104
    self.drawer = ImageDraw.Draw(self.canvas)

  def text(self, xy, text):
    self.drawer.text(xy, text, fill=0)

  def line(self, xy, width):
    self.drawer.line(xy, fill=0, width=1)

  def draw(self):
    self.canvas = self.canvas.transpose(method=Image.ROTATE_180)
    buffer = self.epd.getbuffer(self.canvas)
    self.epd.pwndisplay(buffer)

  def clear(self):
    self.generate_canvas()
    self.epd.pwnclear()
