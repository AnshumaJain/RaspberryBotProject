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
      self.delay = .03
      
   def stop_car(self):
      gpio.output(15, False)
      gpio.output(11, False)
      gpio.output(13, False)
      gpio.output(16, False)

   def forward(self):
      gpio.output(15, False)
      gpio.output(11, True)
      gpio.output(13, True)
      gpio.output(16, False)
      time.sleep(self.delay)

   def reverse(self):
      gpio.output(15, True)
      gpio.output(11, False)
      gpio.output(13, False)
      gpio.output(16, True)
      time.sleep(self.delay)

   def turn_left(self):
      gpio.output(15, False)
      gpio.output(11, True)
      gpio.output(13, False)
      gpio.output(16, False)
      time.sleep(self.delay)

   def turn_right(self):
      gpio.output(15, False)
      gpio.output(11, False)
      gpio.output(13, True)
      gpio.output(16, False)
      time.sleep(self.delay)

   def key_controller(self, key_press):
      if key_press.lower() == 'w':
        self.forward()
      elif key_press.lower() == 's':
        self.turn_right()
      elif key_press.lower() == 'a':
        self.turn_left()
      elif key_press.lower() == 'z':
        self.reverse()
      elif key_press.lower() == 'q':
        self.stop_car()
        # gpio.cleanup()
      else:
        print "wrong input!"


if __name__ == "__main__":
   my_bot = CarBot()
   input_key = sys.argv[1]
   my_bot.key_controller(input_key)
