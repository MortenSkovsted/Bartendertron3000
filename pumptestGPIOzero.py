from gpiozero import LED
import time
led = 25
pump1 = LED(led)
#pump2 = LED
pump1.off()
time.sleep(1)
pump1.on()
