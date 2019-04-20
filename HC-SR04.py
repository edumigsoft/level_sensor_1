import machine
import utime


while True:
  trig=machine.Pin(5, machine.Pin.OUT)
  utrig.off()
  utime.sleep_us(2)
  trig.on()
  utime.sleep_us(10)
  trig.off()
  echo=machine.Pin(4, machine.Pin.IN)
  while echo.value() == 0:
    pass
  t1 = utime.ticks_us()
  while echo.value() == 1:
    pass
  t2 = utime.ticks_us()
  cm = (t2 - t1) / 58.0
  print(cm)
  utime.sleep(2)
