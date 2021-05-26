import socket

class message_client:
    def send():
        try:
            client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
            print("소켓 생성")
        except socket.error as e :
            print("***** 클라이언트 소켓 생성 에러발생 *****")
            print("원인 : " + e)

        HOST = 'ec2-52-79-233-24.ap-northeast-2.compute.amazonaws.com'
        #'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com'
        PORT = 8282
        client_s.connect((HOST,PORT))  # 호스트,포트로  서버에 연결

        # 처음 수신 확인 진행 
        while 1:
            client_message = input("보낼 문자를 입력해 주세요 : ")

            client_s.sendall(client_message.encode('utf-8'))

            # 수신 대기 
            server_receive = client_s.recv(1024)  # 
            
            # 데이터 수신
            server_message = repr(server_receive.decode('utf-8'))

            print("수신 문자 : ", server_message)

            # 지금은 halt를 전송하면 서버랑, 클라이언트랑 동시 종료
            # # 앞으로는 들어가야할 정보가 모두 전송되면 클라이언트는 연결해제 서버는 계속 동작
            if server_message == 'halt':
                break

        client_s.close()