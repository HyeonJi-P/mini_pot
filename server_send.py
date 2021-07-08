import socket
import json

# 0. base
'''
* 호출시 임포트
from server_send import *

* dict를 json형으로 변환
json_insert_data = json.dumps(data)

* json을 dict형으로 변환
json_updata_data = json.loads(data)
'''

class server_send:
    # 함수종류
    ### send 

    # 전체적인 구조
    ### 1. 소켓을 생성
    ### 2. 송신데이터에 명령데이터 추가
    ### 3. 송신할 데이터 json으로 형 변환
    ### 4. 데이터 송신
    ### 5. 데이터의 확인을 위해서(TCP) 재수신을 받음
    ### 6. ++ 송수신 데이터 확인후 조치 취하기 
    ### 7. 연결 끊고 종료

    @staticmethod
    def send(order, send_data):

        # 통신을 위한 소켓 생성
        ## ipv4, tcp 형식 사용
        server_send = socket.socket(socket.AF_INET, sockest.SOCK_STREAM)

        # 소켓을 호스트, 포트를 사용하여 연결
        ## !! 포트는 8282로 설정 (RPi에 포트포워딩 추가해야함)
        ## !! host는 AWS인스턴스 끌때마다 바뀌니까 참고
        HOST = 'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'
        PORT = 8282
        server_send.connect((HOST,PORT))

        # 송신데이터에 명령어 추가
        ## ++ 구분 : sensing, sensing update, change plant, report
        ## !! RPi->server 은 order이 잴 위에 위치
        ## !! server->RPi 는 order이 잴 뒤에 위치
        send_data['ORDER'] = order

        # 받은 dict를 json으로 변경 
        send_data = json.dumps(send_data)

        # 데이터 인코드, 송신 
        server_send.sendall(send_data.encode('utf-8'))

        # 확인 데이터 수신, 디코드
        recv_data = server_send.recv(1024)
        recv_data = repr(recv_data.decode('utf-8'))

        # 송신한 데이터 재수신 받아서 재수신을 할지 말지 판단 
        ## ++ 이 부분은 설계부분에서 다시해서 재활용 해야함 
        if send_data != recv_data:
            #print("재수신 필요함")
        
        # 종료 
        server_send.close()


# test space ----------------------------------------
''''''
