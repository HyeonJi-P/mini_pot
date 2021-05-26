import socket

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

# accept에서 대기하다 client 나타나면 새로운 소켓 리턴
client_s, address = server_s.accept()

print("연결 완료 : ", address)

while 1:

    # 수신, 디코드, dict화
    client_message = client_s.recv(1024)  # 1024byte
    decode_message = client_message.decode('utf-8')
    dict_message = json.loads(decode_message)
    
    # db에 저장
    #sql_sever.insert(dict_message)

    print("데이터 수신완료 : ", address, decode_message)
    client_s.sendall(client_message)

    #server_s.sendall("서버가 클라이언트 에게 hello".encode('utf-8'))
    # 지금은 한번만 실행
    break

server_s.close()
client_s.close()