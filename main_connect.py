'''import RPi.GPIO as GPIO
import spidev'''
import time

from message_client import *
from sql_client import *
'''
GPIO.setmode(GPIO.BCM)
ACT = 47  # onboard led
GPIO.setup(ACT, GPIO.OUT)
'''
try:
    while 1:

        # message_client 호출해서 데이터 보내기, 받기
        # 보내기는 일방적으로 보낸다고 치고
        # 갱신을 위한 데이터를 받는거는? 주기적으로 message_client호출해서 확인?
        # 아니면 음 일단

        # 현제 해야할일
        ## 1. 각각 장치에 mysql설치후 테이블 생성, 갱신작업하는 코드 생성
        ## 2. 메세지 주고받을때 json + image(file) 형식 사용하기
        #### 2-2. 멀티 쓰레딩 준비하기
        ## 3. 했던거 이 코드로 불러와서 전체 테스트하기 

        sql_client.first()



except KeyboardInterrupt:
    print("keyboard out")
    '''
    GPIO.output(ACT, GPIO.LOW)
    GPIO.cleanup()
    '''
