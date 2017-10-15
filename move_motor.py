# Servo Control
import time
import wiringpi

class Chime:
  def __init__(self):
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()

    # set #18 to be a PWM output
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    # divide down clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

  def ring(self):
    delay_period = 0.0075
    for pulse in range(50, 200, 1):
      wiringpi.pwmWrite(18, pulse)
      time.sleep(delay_period)
    for pulse in range(200, 50, -1):
      wiringpi.pwmWrite(18, pulse)
      time.sleep(delay_period)
