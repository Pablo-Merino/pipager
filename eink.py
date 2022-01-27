import epd2in13bc_custom
import time
import pager_canvas
from datetime import datetime
import threading
import os

VERSION = "PiPager 0.0.1"
FILE = "./test.txt"
def current_time():
  return datetime.now().strftime("%d/%m/%Y %H:%M")

screen_details = {
  "time": current_time(),
  "second_line": VERSION,
  "message_line": "aaa",
}

def generate_view(canvas):
  print("redrawing...")
  print(screen_details)
  canvas.clear()
  canvas.text((1,0), screen_details["time"])
  canvas.text((1,93), screen_details["second_line"])
  canvas.text((1,13), screen_details["message_line"])
  canvas.line([0, 12, 212, 12], 1)
  canvas.line([0, 92, 212, 92], 1)
  canvas.draw()

class DisplayUpdater(threading.Thread):
  def __init__(self, canvas):
    threading.Thread.__init__(self)
    self.canvas = canvas
    self.kill_received = False

  def run(self):
    print('thread starting')
    while not self.kill_received:
      time.sleep(60)
      print('thread updating')
      screen_details["time"] = current_time()
      generate_view(canvas)
    print("stopping thread")

try:
  epd = epd2in13bc_custom.EPD()
  epd.init()
  epd.Clear()

  canvas = pager_canvas.Canvas(epd)
  generate_view(canvas)

  t = DisplayUpdater(canvas)
  t.daemon = True
  t.start()

  original_time = os.path.getmtime(FILE)
  while True:
    if(os.path.getmtime(FILE) > original_time):
      with open(FILE, 'r') as f:
        print('detected new message')
        message = f.read()
        screen_details["message_line"] = message
        generate_view(canvas)
      original_time = os.path.getmtime(FILE)
    time.sleep(1)
  
except KeyboardInterrupt:
  print('exiting display updater thread...')
  t.kill_received = True

  print('clearing display...')
  canvas.clear()
  canvas.clear()
  epd2in13bc_custom.epdconfig.module_exit()
  print('good bye!')
  exit()

