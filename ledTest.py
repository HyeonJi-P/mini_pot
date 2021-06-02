import time
import smbus
import RPi_I2C_driver
import RPi.GPIO as GPIO

'''
LED색
R+G+B=흰색
R+G=노랑
G+B=청록
R+B=마젠타
'''

class ledTest:

    RGB_LED_R=5 #RGB LED
    RGB_LED_G=6
    RGB_LED_B=13

    @classmethod
    def on():
        GPIO.setup(RGB_LED_R,GPIO.OUT, initial = GPIO.LOW) #출력으로 설정, 시작값 low(꺼짐)
        GPIO.setup(RGB_LED_G,GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(RGB_LED_B,GPIO.OUT, initial = GPIO.LOW)

        GPIO.output(RGB_LED_R,GPIO.LOW) #초기화 
        GPIO.output(RGB_LED_G,GPIO.LOW)
        GPIO.output(RGB_LED_B,GPIO.LOW)
        time.sleep(1)

        GPIO.output(RGB_LED_R,GPIO.HIGH) #빨강불
        GPIO.output(RGB_LED_G,GPIO.LOW)
        GPIO.output(RGB_LED_B,GPIO.LOW)
        time.sleep(3)

    @classmethod
    def status():
        time.sleep(3)

    @classmethod
    def control(control_data):
        LED_R = control_data['LED_R']
        LED_G = control_data['LED_G']
        LED_B = control_data['LED_B']

        if LED_R == 1:
            GPIO.output(RGB_LED_R,GPIO.HIGH)
        else:
            GPIO.output(RGB_LED_R,GPIO.LOW)

        if LED_G == 1:
            GPIO.output(RGB_LED_G,GPIO.HIGH)
        else:
            GPIO.output(RGB_LED_G,GPIO.LOW)
        
        if LED_B == 1:
            GPIO.output(RGB_LED_B,GPIO.HIGH)
        else:
            GPIO.output(RGB_LED_B,GPIO.LOW)

        time.sleep(3)