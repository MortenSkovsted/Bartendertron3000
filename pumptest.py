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