import socket

try:
    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
    print("소켓 생성")

except socket.error as e :
    print("***** 소켓 생성 에러발생 *****")
    print("원인 : " + e)

HOST = 'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'
PORT = 8282
client_s.connect((HOST,PORT))  # 호스트,포트로  서버에 연결

while 1:

    client_message = input("보낼 문자를 입력해 주세요 : ")

    client_s.sendall(client_message.encode('utf-8'))

    server_receive = client_s.recv(1024)
    print("수신 문자 : ", repr(server_receive.decode('utf-8')))

    if client_message.decode('utf-8') == 'halt':
        break

client_s.close()