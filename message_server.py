import socket
import json
from sql_server import sql_server
import pymysql

# 현제 이 소스는 recv() 형태 

try:
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
    print("소켓 생성")
except socket.error as e :
    print("***** 서버 소켓 생성 에러발생 *****")
    print("원인 : " + e)

HOST = 'ec2-3-35-233-185.ap-northeast-2.compute.amazonaws.com'
#'ec2-52-79-233-24.ap-northeast-2.compute.amazonaws.com' -p
#'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com' -k
PORT = 8282
server_s.bind((HOST,PORT))  # 소켓을 호스트와 포트에 연결
server_s.listen(2)  # 클라이언트에게 들을 준비 완료 (동시접속 2허용)

# accept에서 대기하다 client 나타나면 새로운 소켓 리턴
client_s, address = server_s.accept()

print("연결 완료 : ", address)

while 1:

    # 데이터 수신
    client_message = client_s.recv(1024)  # 1024byte 데이터 수신
    decode_message = client_message.decode('utf-8')  # 수신 데이터 decode
    dict_message = json.loads(decode_message)  # 받은 json데이터를 dict형으로 변환
    
    # db에 저장
    #sql_server.insert(dict_message)

    # 일련의 과정 테스트를 위한 데이터 가공 # 임시용 원래는 다른 실행 파일 호출해야함 ------------
    LED_R = dict_message['LED_R']
    LED_G = dict_message['LED_G']
    LED_B = dict_message['LED_B']
    
    if LED_R > 0.1:
        LED_R = 0.1
    else: 
        LED_R = 0.9
    if LED_G > 0.1:
        LED_G = 0.1
    else: 
        LED_G = 0.9
    if LED_B > 0.1:
        LED_B = 0.1
    else: 
        LED_B = 0.9

    dict_message['LED_R'] = LED_R
    dict_message['LED_G'] = LED_G
    dict_message['LED_B'] = LED_B

    server_message = json.dumps(dict_message)  # dict를 다시 json으로 변환
    # -------------------------------------------------------------------------------------

    # 데이터 수신 확인을 위한 재전송 # 지금은 조금 변형해서 주는 1회성 UDP 방식으로 
    print("데이터 수신완료 : ", address, client_message)
    #client_s.sendall(client_message)
    client_s.sendall(server_message)  # <<-



    # 지금은 한번만 실행
    break

server_s.close()
client_s.close()