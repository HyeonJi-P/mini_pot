import socket
import json

class message_client:
    def send(result_data):
        # 받은 dict형을 json으로 변환
        json_insert_data = json.dumps(result_data)

        try:
            client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4, tcp 형식 사용
            print("소켓 생성")
        except socket.error as e :
            print("***** 클라이언트 소켓 생성 에러발생 *****")
            print("원인 : " + e)

        HOST = 'ec2-3-35-233-185.ap-northeast-2.compute.amazonaws.com'
        #'ec2-52-79-233-24.ap-northeast-2.compute.amazonaws.com' -p
        #'ec2-15-165-203-96.ap-northeast-2.compute.amazonaws.com' -k
        PORT = 8282
        client_s.connect((HOST,PORT))  # 호스트,포트로  서버에 연결
        print("호스트, 포트 : 서버 연결완료")
        
        # 데이터 송수신
        while 1:
            
            # 데이터 송신
            client_message = json_insert_data
            client_s.sendall(client_message.encode('utf-8'))

            # 데이터 수신 대기 
            server_receive = client_s.recv(1024)
            # 데이터 수신
            server_message = repr(server_receive.decode('utf-8'))

            # 송신데이터와 수신데이터를 비교해서 차이점이 있다면 다시 실행해야함
            ## 하지만 일단 수신 udp라 치고 그냥 진행
            print("수신 문자 : ", server_message)
            '''
            # 지금은 halt를 전송하면 서버랑, 클라이언트랑 동시 종료
            # # 앞으로는 들어가야할 정보가 모두 전송되면 클라이언트는 연결해제 서버는 계속 동작
            if server_message == 'halt':
                break
            '''
            # 일단 한번만돌고 나가는걸로 
            break

        client_s.close()