import time
import json
import pandas as pd

from sql_server import *

# todo (thinking + algorithme)
### ++ 에러사항 대처 필요함 (정시에 작동하는 코드 송-수신 오류시 재전송, 식물 불일치...)
### ++ 송수신 데이터에 분류타입 추가
### ++ 정시 작동과 반복 작동의 분할 실행법
### ++ a

# todo (code file)
### S-recv, save, S-send main에 맞게 설정 + 추가 계발 (사실 에내도 위에 todo 보면 거의 0.. 아니다 1부터 시작하는...)
### manufacture, report: 0부터 시작하는 이세계 여행

'''main 코드 설명'''
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
        


        # 지금은 1회 테스트 
        break

except KeyboardInterrupt:
    print("!! process down (KeyboardInterrupt)")