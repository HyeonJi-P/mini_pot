import socket
import os
import sys

try:
    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
    print("소켓 생성")
except socket.error as e :
    print("***** 클라이언트 소켓 생성 에러발생 *****")
    print("원인 : " + e)

HOST = 'ec2-52-79-235-57.ap-northeast-2.compute.amazonaws.com'
#'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'
PORT = 8282
client_s.connect((HOST,PORT))  # 호스트,포트로  서버에 연결

# 처음 수신 확인 진행 
while 1:
    client_filename = input("전송할 파일 이름을 입력해 주세요 : ")

    client_s.sendall(client_filename.encode('utf-8'))

    # 수신 대기 
    data = client_s.recv(8096)  # 
    data_transferred = 0
    # 데이터 수신
    #server_message = repr(server_receive.decode('utf-8'))

    #print("수신 문자 : ", server_message)

    if not data :
        print('파일 %s가 서버에 존재하지않음' %client_filename)
        break

    nowdir = os.getcwd()
    with open(nowdir+"\\"+client_filename,'wb') as f: #현재 dir에 filename으로 파일을 받는다
        try:
            print("try문")
            while data: #데이터가 있을 때 까지
                print("while문")
                f.write(data)
                data = client_s.recv(8096)
                
                 
                
        except Exception as ex:
            print(ex)
        f.close()
        print('파일 %s 받기 완료. ' %(client_filename))


client_s.close()