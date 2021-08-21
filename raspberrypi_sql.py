import pymysql
import pandas as pd

# 0. base
'''
* 호출시 임포트
from respberrypi_sql import *
'''

# 1. insert : dict형을 받아서 디비에 저장해준다.
'''
* 들어가는 자료형 예시
dict_message = {
    'time' : '2000-11-22 11:22:33',
    'plant' : 'baechu',
    'temperature': 21,
    'humidity': 6,
    'illuminance': 24.13
}
'''

# 2. 갱신요청시 새로운 데이터 송신

# 3. 서버로부터 생장조건을 받고 라즈베리파이에서 조회할 수 있게끔 

class respberrypi_sql:

    @staticmethod
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8') # 예전 비번 : *6CC6A1C22CFFA93B23769CAE343636557E024D12
        try:
            # cur = conn.cursor()랑 같은 의미
            with conn.cursor() as cur:

                # DB에 쿼리로 데이터 추가
                
                # dict형의 key값을 리스트로 변환 (valuse()를 호출하기 위해서)
                col_list = list(insert_data.keys())

                # key_list를 문자열으로 변환 (디비에 적용하기 위해서)
                col = ', '.join(col_list)

                # 위와 같이 valuse도 진행하면 정수형과 문자열이 구분이 안되기 때문에
                # 앞서 진행한 key_list로 dict에 각각 접근하여 문자열은 따움표로 감싸고 나머지는 그냥 join
                ## val = ','.join(map(str, insert_data.values())) <== 이렇게하면 문자열이 ''로 안둘려서 나옴
                val = ""
                for i in col_list:
                    col_data = insert_data[i]
                    if str(type(col_data)) == "<class 'str'>":  # str이면 '추가
                        val += "'"
                    val += str(col_data)
                    if str(type(col_data)) == "<class 'str'>":
                        val += "'"
                    val += ", "
                val = val[0:-2]

                # key값과 value값을 전달하여 진행
                query = "INSERT INTO mytable(%s) VALUES(%s);" %(col, val)
                cur.execute(query)

                conn.commit()
        finally:
            conn.close()

# test space ----------------------------------------
''''''
