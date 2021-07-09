import time
import json
import pandas as pd

from server_recv import *
from server_sql import *
from server_report import *
from server_send import *

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

print("!! process start \n")
try:
    while 1:
        # 전체적인 구조
        ### 1. 정시에 작동되는 프로세스 실행
        ##### 1. 생장조건 갱신 << ++ table 설계 이후 << ++ 회원과 연결, ++ 다중 배포
        ##### 2. 보고서 작성 << ++ 보고서용 데이터 추출(형식필요)이후 << 그에 맞게 이미지 생성, docx에 붙이기, file 전송
        ### 2. RPi로 부터 메시지 수신
        ##### 1. 메시지 수신, 변환, 가공 << ++ 정시 작동을 위해 특정 시간에는 빠져 나오도록? 하거나 추가 설정이 필요함
        ##### 2. 수신 데이터 분기점 시작 [ 정시보고(센싱), 사용자 요청 갱신(센싱+보고서), 식물변경, 보고서요청 ]
        ####### 1. 정시보고(센싱)
        ####### 2. 수시보고(센싱+보고서) << ++ 보고서 마무리, ++ 송신 마무리
        ####### 3. 식물변경 << ++ sql에서 새로운 함수 만들어서 전송하기
        ####### 4. 보고서 요청 << ++ RPi의 송수신, main만들어서 해봐야함


        # 1-1, 2-1, 2-2-2,3,4
        # ++ 전체 함수에 인자값 추가해서 돌아가는 식으로 생성
        # ++++ 송신 부분에 order 추가



        # 정시 작동 - - - - - - - - - -
        ## ++ recv에 해당 시간이 되면 메인으로 빠져나오는게 필요함
        ## ++ 너무 계속해서 반복할 필요는 없으니까 while의 반복 횟수 같은 걸로 조절해보기 (완성후)
        now_time = time.localtime(time.time())
        if now_time.tm_hour == 17:
            # 생장조건 갱신 (5시)
            # ++ 모든 회원의 식물을 조회하여 변경점이 생긴 식물을 가지고 있는 기기에 송신
            server_sql.plant_guide() # 생장조건이 변경된 모든 식물 조회, 그 식물을 소지한 모든 회원에게 보낼 데이터 만들기
            server_send.send() # 생장 조건을 모든 회원의 RPi로 송신
        if now_time.tm_hour == 18:
            # 보고서 정시 작성 (6시)
            server_sql.report_data() # 보고서용 데이터를 가져와서 (++ dict???)
            document_make.word_form() # 보고서를 만들고 (++ 경로반환???)
            server_send.send() # 송신 (++ file socket 사용?, ++ 안드로이드 부분 정립후 다시 해야함)
        

        
        # raspberrypi_message를 수신 - - - - - - - - - -
        ## 데이터 가공 : json을 dict로 변환, ORDER부분은 따로 추출
        ## ++ ORDER : sensing, sensing update, change plant, report
        ## ++ ORDER : plant guide, sensing update, report
        order, recv_data = server_recv.recv()

        # ++ recv중에서 받아오는 시간의 제한을 두고 받은 데이터가 없다면 order을 pass로 줘서
        # 분류지시를 넘어가게끔 전체 if문을 걸기
        # ++ recv에 해당 시간이 되면 메인으로 빠져나오는거의 대안점? 



        # order으로 작업 분류 지시 - - - - - - - - - -
        # 수신 데이터 : 센싱데이터 수신, 센싱+보고서
        if (order == "sensing") or (order == "sensing update"):
            # 일반 센싱 데이터 수신이면 저장만 하고 끝
            server_sql.insert(recv_data)

            # 센싱 + 보고서일 경우 바로 보고서 제작 
            if order == "sensing update":
                server_sql.report_data() # 보고서용 데이터 추출 
                document_make.word_form() # 보고서 제작
                server_send.send() # 보고서 송신 
        
        # 수신 데이터 : 식물 변경 요청
        elif order == "change plant":
            # ++ server_sql에  소스추가, 테이블 생성
            ## ++ 단순 변경이 아니라 정시 호출이라면 해당 설계 다시 할 필요가 있음
            ## => 현제 사용자의 식물 정보를 어디서 가져와야 할지 판단이 불가능함
            ## 고로 회원가입을 만들고 사용자 테이블을 만들어서 거기에 식물 정보를 저장하고 조회해야함

            # 단순 변경은 받은 string 값으로 생장조건을 조회한다음 그 값을 send로 전달해주면 됨
            server_sql.plant_change()
            server_send.send()

        # 수신 데이터 : 보고서 요청
        elif order == "report":
            # RPi에 갱신요청
            server_send.send("report", recv_data) # !! recv에서 order만 있는 경우 빈 dict가 생성됨 진행 가능?








        # 지금은 1회 테스트 
        break

except KeyboardInterrupt:
    print("!! process down (KeyboardInterrupt)")
print("\n!! process end")

# test space ----------------------------------------
''''''
