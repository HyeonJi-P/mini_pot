import RPi.GPIO as GPIO
import spidev
import time

#from message_client import *
#from sql_client import *

GPIO.setmode(GPIO.BCM)

ACT = 47  # onboard led
GPIO.setup(ACT, GPIO.OUT)

try:
    while 1:
       GPIO.output(ACT, GPIO.HIGH)
       time.sleep(2)
       GPIO.output(ACT, GPIO.LOW)
       time.sleep(2)

except KeyboardInterrupt:
    print("keyboard out")
    GPIO.output(ACT, GPIO.LOW)
    GPIO.cleanup()
