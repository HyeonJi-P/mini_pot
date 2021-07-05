import time
import json
import pandas as pd

from server_recv import *
from server_sql import *
from document_make import *

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

        # ++ 송신때 order을 추가로 더해서 보내줘야함
        ## ++ ORDER : plant guide, sensing update, report
        ## ++ order안 겹치게? 



        # 정시 작동 - - - - - - - - - -
        ## ++ recv에 해당 시간이 되면 메인으로 빠져나오는게 필요함
        ## ++ 너무 계속해서 반복할 필요는 없으니까 while의 반복 횟수 같은 걸로 조절해보기 (완성후)
        now_time = time.localtime(time.time())
        if now_time.tm_hour == 17:
            # 생장조건 갱신 (5시)
            ## ++ 생장 조건 table에서 사용자에 맞는 식물을 보내줘야함 
            ## ++++ 생장 조건 table이 변경 되었을때 하는게 좋음
            server_sql.plant_guide() 
            server_send.send() # 생장 조건을 RPi로 송신
        if now_time.tm_hour == 18:
            # 보고서 정시 작성 (6시)
            server_sql.report_data()
            document_make.word_form()
            server_send.send()
        

        
        # raspberrypi_message를 수신 - - - - - - - - - -
        ## 데이터 가공 : json을 dict로 변환, ORDER부분은 따로 추출
        ## ++ ORDER : sensing, sensing update, change plant, report
        order, recv_data = server_recv.recv()

        # ++ recv중에서 받아오는 시간의 제한을 두고 받은 데이터가 없다면 order을 pass로 줘서
        # 분류지시를 넘어가게끔 전체 if문을 걸기
        # ++ recv에 해당 시간이 되면 메인으로 빠져나오는거의 대안점? 



        # order으로 작업 분류 지시 - - - - - - - - - -
        # 수신 데이터 : 센싱데이터 수신, 센싱+보고서
        if (order == "sensing") or (order == "sensing update"):
            # 일반 센싱 데이터 수신이면 저장만 하고 끝
            server_sql.insert_data()

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
            server_sql.plant()
            server_send.send()

        # 수신 데이터 : 보고서 요청
        elif order == "report":
            # RPi에 갱신요청
            server_send.send() # ++ server_send:소스코드 생성








        # 지금은 1회 테스트 
        break

except KeyboardInterrupt:
    print("!! process down (KeyboardInterrupt)")
print("\n!! process end")

# test space ----------------------------------------
''''''
