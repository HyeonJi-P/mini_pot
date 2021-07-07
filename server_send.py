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

class server_recv:
    # 함수종류
    ### send 

    # 전체적인 구조
    ### 1. 소켓을 생성
    ### 2. 데이터를 수신 (json)
    ### 3. json데이터를 dict로 변환
    ### 4. dict중 명령 데이터를 분리
    ### 5. 수신 데이터의 확인차 수신 데이터 재 전송
    ### 6. 연결 끊고 반환

    @staticmethod
    def send():

        # ++ 혹시 안될경우 재시도하는 횟수 << keep
        #retry_times = 10

        # 통신을 위한 소켓 생성
        ## ipv4, tcp 형식 사용
        server_recv = socket.socket(socket.AF_INET, sockest.SOCK_STREAM)

        # 소켓을 호스트, 포트를 사용하여 연결
        ## !! 포트는 8282로 설정 (AWS에 포트포워딩 추가해야함)
        ## !! host는 AWS인스턴스 끌때마다 바뀌니까 참고
        HOST = 'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'
        PORT = 8282
        server_recv.bind((HOST,PORT))

        # 클라이언트에게 들을 준비 완료
        ## 동시접속 5허용
        server_recv.listen(5)

        # accept에서 대기하다 raspberrypi 나타나면 새로운 소켓 리턴
        raspberrypi_send, address = server_recv.accept()

        # 데이터 수신
        raspberrypi_message = raspberrypi_send.recv(1024)  # !! 1024byte 데이터 수신 (데이터량 증가시 변경 필요)

        # 수신 데이터 decode 
        decode_message = raspberrypi_message.decode('utf-8')

        # 수신 데이터 형 변환 (json -> dict)
        dict_message = json.loads(decode_message)

        # 수신 데이터에서 명령 데이터와 내부데이터로 분리
        ## pop로 하면 바로 삭제하고 반환이긴한데 이게 좀 더 가시적인거 같음 아마?
        ### ++ 구분 : sensing, sensing update, change plant, report
        order = dict_message['ORDER']
        del dict_message['ORDER']

        # TCP니까 확인을 위해서 받은내용 재전송
        ### ++ 받은쪽에서 만약 데이터가 틀리다면 서버에 재전송 하고 서버는 그걸 처리해야함
        raspberrypi_send.sendall(raspberrypi_message)

        # 연결 끊음
        server_recv.close()
        raspberrypi_send.close()

        # 반환해주고 끝~
        return order, dict_message


# test space ----------------------------------------
''''''
