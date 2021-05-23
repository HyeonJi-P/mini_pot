import socket
from os.path import exists
import sys

try:
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
    print("소켓 생성")
except socket.error as e :
    print("***** 서버 소켓 생성 에러발생 *****")
    print("원인 : " + e)

HOST = 'ec2-52-79-233-24.ap-northeast-2.compute.amazonaws.com'
#'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'

PORT = 8282
server_s.bind((HOST,PORT))  # 소켓을 호스트와 포트에 연결
server_s.listen(2)  # 클라이언트에게 들을 준비 완료 (동시접속 2허용)

client_s, address = server_s.accept()  # accept에서 대기하다 client 나타나면 새로운 소켓 리턴

print("연결 완료 : ", address)

while 1:

    print(str(address),'에서 접속')
    # 클라이언트 메세지 수신 대기 
    filename = client_s.recv(1024)  # 1024byte
    print('요청받은 데이터: ', filename.decode('utf-8'))
    data_transferred = 0

    if not exists(filename):
        print('no file')
        break

    print("파일 전송 시작")
    with open(filename, 'rb') as f:
        try :
            data = f.read(1024)
            while data:
                data_transferred += client_s.sendall(data)
                data = f.read(1024)
        except Exception as ex:
            print(ex)
    print("전송완료")


    

    #server_s.sendall("서버가 클라이언트 에게 hello".encode('utf-8'))

server_s.close()
client_s.close()