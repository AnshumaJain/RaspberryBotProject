import time
import sys

import RPi.GPIO as gpio

# IN1-5V, IN2-GND = motorA forward
# IN1-GND, IN2-5V = motorA reverse
# IN3-5V, IN4-GND = motorB forward
# IN3-GND, IN4-5V = motorB reverse

class CarBot:

   def __init__(self):
      gpio.setwarnings(False)
      gpio.setmode(gpio.BOARD)
      gpio.setup(15, gpio.OUT)  #IN4 # MotorB Control
      gpio.setup(11, gpio.OUT) #IN3 # MotorB Control
      gpio.setup(13, gpio.OUT)  #IN2 MotorA Control
      gpio.setup(16, gpio.OUT) #IN1 MotorA Control

   def stop(self):
      gpio.output(15, False)
      gpio.output(11, False)
      gpio.output(13, False)
      gpio.output(16, False)

   def forward(self, tf):
      gpio.output(15, False)
      gpio.output(11, True)
      gpio.output(13, True)
      gpio.output(16, False)
      time.sleep(tf)

   def reverse(self, tf):
      gpio.output(15, True)
      gpio.output(11, False)
      gpio.output(13, False)
      gpio.output(16, True)
      time.sleep(tf)

   def turn_left(self, tf):
      gpio.output(15, False)
      gpio.output(11, True)
      gpio.output(13, False)
      gpio.output(16, False)
      time.sleep(tf)

   def turn_right(self, tf):
      gpio.output(15, False)
      gpio.output(11, False)
      gpio.output(13, True)
      gpio.output(16, False)
      time.sleep(tf)

   def key_controller(self, char):
      key_press = char
      st = .03

      if key_press.lower() == 'w':
        self.forward(st)
      elif key_press.lower() == 's':
        self.turn_right(st)
      elif key_press.lower() == 'a':
        self.turn_left(st)
      elif key_press.lower() == 'z':
        self.reverse(st)
      elif key_press.lower() == 'q':
        self.stop()
        # gpio.cleanup()
      else:
        print "wrong input!"


if __name__ == "__main__":
   ob = CarBot()
   input = sys.argv[1]
   ob.key_controller(input)
