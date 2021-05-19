import socket

try:
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
    print("소켓 생성")

except socket.error as e :
    print("***** 소켓 생성 에러발생 *****")
    print("원인 : " + e)

HOST = 'localhost'
PORT = 8282
server_s.bind((HOST,PORT))  # 소켓을 호스트와 포트에 연결
server_s.listen(2)  # 클라이언트에게 들을 준비 완료 (동시접속 2허용)

client_s, address = server_s.accept()  # accept에서 대기하다 client 나타나면 새로운 소켓 리턴

print("연결 완료 : ", address)

while 1:

    # 클라이언트 메세지 수신 대기 
    client_message = client_s.recv(1024)  # 1024byte

    decode_message = client_message.decode('utf-8')

    if decode_message == 'halt':
        break

    print("데이터 수신완료 : ", address, decode_message)

    client_s.enddall(client_message)

    #server_s.sendall("서버가 클라이언트 에게 hello".encode('utf-8'))

server_s.close()
client_s.close()