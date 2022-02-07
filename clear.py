import epd2in13bc_custom
import time
epd = epd2in13bc_custom.EPD()
epd.init()

for i in range(0, 10):
  print(f"clear {i}")
  epd.pwnclear()
  print(f"sleep {i}")
  time.sleep(5)
