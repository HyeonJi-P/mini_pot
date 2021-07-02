import time
import json
import pandas as pd

from server_recv import *
from server_sql import *

# 정시 작동 함수 실행
''''''
# 데이터 수신 [S-recv] 
### 센싱데이터 수신 (from R-send >> to save)
### 보고서갱신-센싱데이터 수신 (from R-send >> to save)
### 식물종류 변경요청 수신 (from User >> to save)
### 보고서 요청 수신 (from User >> to S-send)
''''''
# 데이터 저장 [save]
### 센싱 데이터 저장 (from S-recv >> to DB) // => 정시작동 (from DB >> to manufacture)
### 보고서갱신-센싱데이터 저장 (from S-recv >> to manufacture)
### 생장조건 저장 (from Admin)
### 생장조건(식물종류변경) 조회 (from S-recv >> to S-send)
### 생장조건(변동사항 유) 전달 (from DB >> to S-send) // 정시작동
''''''
# 데이터 가공 [manufacture]
### 보고서 데이터 가공 (from save >> to report)
''''''
# 데이터 생성 [report]
### 보고서 생성 (from manufacture >> to S-send)
''''''
# 데이터 송신 [S-send]
### 생장조건 송신 (from save >> to R-recv) // 정시작동
### 보고서용 갱신요청 송신 (from S-recv >> to R-recv)
### 보고서 송신 (from report >> to User)

print("!! process start")
try:
    while 1:
        dict_message = {
            'time' : '2000-11-22 11:22:33',
            'plant' : 'baechu',
            'temperature': 21,
            'humidity': 6,
            'illuminance': 24.13
        }
        dict_message = json.dumps(dict_message)

        rec = server_recv.recv(dict_message)
        
        print(rec)
        


        # 지금은 1회 테스트 
        break

except KeyboardInterrupt:
    print("!! process down (KeyboardInterrupt)")

print("!! process end")
