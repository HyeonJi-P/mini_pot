# 나중에 쓰일수 있는 계륵같은 코드

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
       GPIO.output(ACT, GPIO.HIGH)  # False , True
       time.sleep(1)
       GPIO.output(ACT, GPIO.LOW)
       time.sleep(1)

except KeyboardInterrupt:
    print("keyboard out")
    GPIO.output(ACT, GPIO.LOW)
    GPIO.cleanup()
