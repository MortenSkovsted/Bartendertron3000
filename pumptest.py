<<<<<<< HEAD
import RPi.GPIO as GPIO
import time

led = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
print("On")
GPIO.output(led, GPIO.LOW)
time.sleep(10)
print("Off")
GPIO.output(led, GPIO.HIGH)
=======
from gpiozero import LED
import time
led = 25
pump1 = LED(led)
#pump2 = LED
pump1.off()
time.sleep(1)
pump1.on()
>>>>>>> e1856f4529bc40e669bdbe2a7f00bc1255faaf09
