#import RPi.GPIO as GPIO
#import spidev
import time
import json

from message_client import *
from sql_client import *

#GPIO.setmode(GPIO.BCM)
#ACT = 47  # onboard led
#GPIO.setup(ACT, GPIO.OUT)

try:
    while 1:
        # 결과 저장소 : 지금은 dict 마지막에 전달할때만 json
        result_data = {'time' : '1111-22-33 44:55:66'}
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        result_data['time'] = now_time

        # 여기에 소켓 프로그래밍 
        ###

        # 결과 저장시 방법 : 현제는 임시 데이터
        result_data['plant'] = 'test_plant2'
        result_data['temperature'] = 23
        result_data['humidity'] = 24
        result_data['illuminance'] = 25.2

        # dict 시간 입력 제대로 됬는지 확인
        if result_data['time'] == '1111-22-33 44:55:66':
            print("현제시간 dict입력 실패!")

        # 저장을 위한 파이썬 호출 ==> 나중에 서버에도 해야함
        #sql_client.insert(result_data)

        # 전송을 위한 파이썬 호출 
        message_client.send(result_data)




        # 현제 해야할일
        ## 1. 각각 장치에 mysql설치후 테이블 생성, 갱신작업하는 코드 생성
        ## 2. 메세지 주고받을때 json + image(file) 형식 사용하기
        #### 2-2. 멀티 쓰레딩 준비하기
        ## 3. 했던거 이 코드로 불러와서 전체 테스트하기 

        # 코드순서
        ###1. 센서 데이터 일정시간마다 돌아감 
        ###2. 센싱 데이터 sql에 저장 
        #####2-2. 일단 sql에 저장하는것 보다 바로 전달하는 쪽으로
        ###3.

        # 지금은 한번만
        break

except KeyboardInterrupt:
    print("keyboard out")
    '''
    GPIO.output(ACT, GPIO.LOW)
    GPIO.cleanup()
    '''
