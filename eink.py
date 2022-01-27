import epd2in13bc_custom
import time
import pager_canvas
from datetime import datetime

VERSION = "PiPager 0.0.1"

try:
  time_date = datetime.now().strftime("%d/%m/%Y %H:%M")
  epd = epd2in13bc_custom.EPD()
  epd.init()
  epd.Clear()

  pager_canvas = pager_canvas.Canvas(epd)

  pager_canvas.text((0,0), time_date)
  pager_canvas.text((0,93), VERSION)
  pager_canvas.line([0, 12, 212, 12], 1)
  pager_canvas.line([0, 92, 212, 92], 1)
  pager_canvas.draw()

  while True:
    print('updating')
    time.sleep(60)
    pager_canvas.clear()
    time_date = datetime.now().strftime("%d/%m/%Y %H:%M")
    pager_canvas.text((0,0), time_date)
    pager_canvas.draw()

except KeyboardInterrupt:
  pager_canvas.clear()
  pager_canvas.clear()
  epd2in13bc_custom.epdconfig.module_exit()
  exit()

