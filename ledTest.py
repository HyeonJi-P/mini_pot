import time
import smbus
import RPi_I2C_driver
import RPi.GPIO as GPIO

'''
LED색
R+G=노랑
R+G+B=흰색
G+B=청록
R+B=마젠타
'''



#사용하는 핀 번호들(BCM)
GPIO.setmode(GPIO.BCM) #GPIO 핀에 gpio 1등 이런식으로 쓰인곳기준(아마도)

RGB_LED_R=5 #RGB LED
RGB_LED_G=6
RGB_LED_B=13

GPIO.setup(RGB_LED_R,GPIO.OUT, initial = GPIO.LOW) #출력으로 설정, 시작값 low(꺼짐)
GPIO.setup(RGB_LED_G,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RGB_LED_B,GPIO.OUT, initial = GPIO.LOW)

GPIO.output(RGB_LED_R,GPIO.LOW) #초기화
GPIO.output(RGB_LED_G,GPIO.LOW) #불끄기
GPIO.output(RGB_LED_B,GPIO.LOW)
time.sleep(1)

GPIO.output(RGB_LED_R,GPIO.HIGH) #빨강불
GPIO.output(RGB_LED_G,GPIO.LOW)
GPIO.output(RGB_LED_B,GPIO.LOW)
time.sleep(3)
GPIO.output(RGB_LED_R,GPIO.LOW) #초기화
GPIO.output(RGB_LED_G,GPIO.LOW) #불끄기
GPIO.output(RGB_LED_B,GPIO.LOW)

GPIO.output(RGB_LED_R,GPIO.LOW) #초록
GPIO.output(RGB_LED_G,GPIO.HIGH)
GPIO.output(RGB_LED_B,GPIO.LOW)
time.sleep(3)
GPIO.output(RGB_LED_R,GPIO.LOW) #초기화
GPIO.output(RGB_LED_G,GPIO.LOW) #불끄기
GPIO.output(RGB_LED_B,GPIO.LOW)

GPIO.output(RGB_LED_R,GPIO.LOW) #파랑
GPIO.output(RGB_LED_G,GPIO.LOW)
GPIO.output(RGB_LED_B,GPIO.HIGH)
time.sleep(3)
GPIO.output(RGB_LED_R,GPIO.LOW) #초기화
GPIO.output(RGB_LED_G,GPIO.LOW) #불끄기
GPIO.output(RGB_LED_B,GPIO.LOW)