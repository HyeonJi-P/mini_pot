import time
import smbus
import RPi.GPIO as GPIO

'''
LED색
R+G+B=흰색
R+G=노랑
G+B=청록
R+B=마젠타
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RGB_LED_R=5
RGB_LED_G=6
RGB_LED_B=13

def LedRGB(R, G, B):
    if R == 1:
        GPIO.output(RGB_LED_R,GPIO.HIGH)
    else:
        GPIO.output(RGB_LED_R,GPIO.LOW)
    
    if G == 1:
        GPIO.output(RGB_LED_G,GPIO.HIGH)
    else:
        GPIO.output(RGB_LED_G,GPIO.LOW)

    if B == 1:
        GPIO.output(RGB_LED_B,GPIO.HIGH)
    else:
        GPIO.output(RGB_LED_B,GPIO.LOW)


GPIO.setup(RGB_LED_R,GPIO.OUT, initial = GPIO.LOW) #출력으로 설정, 시작값 low(꺼짐)
GPIO.setup(RGB_LED_G,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RGB_LED_B,GPIO.OUT, initial = GPIO.LOW)

LedRGB(0, 0, 0)
time.sleep(3)

LedRGB(1, 0, 0)
time.sleep(3)

LedRGB(0, 1, 0)
time.sleep(3)

LedRGB(0, 0, 1)
time.sleep(3)

#LedRGB(1, 1, 0)
#time.sleep(3)

#LedRGB(1, 0, 1)
#time.sleep(3)

#LedRGB(0, 1, 1)
#time.sleep(3)

#LedRGB(1, 1, 1)
#time.sleep(3)

GPIO.cleanup()