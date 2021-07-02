import pymysql
import json  # ++ 지금은 안쓰이냄... 이따 연결때 바뀔지 봐야됨
import pandas as pd

# 0. base
'''
* 호출시 임포트
from server_sql import *

* dict를 json형으로 변환
json_insert_data = json.dumps(data)

* json을 dict형으로 변환
json_updata_data = json.loads(data)
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

* 호출시 예시
server_sql.insert(dict_message)
'''
# 1-2. insert_test : int형을 받아서 그 수만큼 자동 삽입 (~100)
'''
!! 주의사항
!! 시간이 고정이기 때문에? 기존 테이블 확인해야함
!! 2000-01-22 11:22:xx - xx부분만 바뀌는거라 max는 100

* 호출 예시
server_sql.insert_test(10)
'''

# 2. select : SQL-query문의 where이후 문자열을 받아서 조회한다.
'''
* 호출 예시
temp = None
temp = "all" // !! temp가 None이거나 "all"일 경우 모든자료 검색
temp = "plant = 'hub'" // plant가 hub인 것만 검색
server_sql.select(temp)
'''

# 3. delete : SQL-query문의 where이후 문자열을 받아서 삭제한다.
'''
* 호출 예시
temp = "time in(SELECT min(time) FROM mytable)" // 시간이 가장 작은(오래된) 행 삭제
server_sql.delete(temp)
'''
# 3-2. db_limite : 라즈베리파이 같은경우 임시 저장소니까 갯수제한을 둬서 행을 삭제 (순서대로-예전데이터) 
'''
* 호출 예시
++ 들어가는 수 부분(10)을 라즈베리파이 메인 소스에서 변수로 지정해 둬서 고정
server_sql.db_limite(10)

++ 추후 디비쪽도 어느정도 데이터의 가공이 필요하다고 생각됨 그때 조금 수정할 가능성 있음
'''

# 4. updata : null
'''
* 아직은 필요 없다고 생각됨
'''

class server_sql:
    # 함수종류
    ### insert
    ### select
    ### delete
    ### db_limite
    ### insert_test
    ### update

    # 전체적인 구조
    ### 1. conn으로 디비에 연결하고
    ### 2. cur = conn.cursor() 으로 커서 사용
    ### 3. cur.execute(Q)으로 Q를 디비에 전달하고 실행
    ### 4. conn.commit()으로 실행내역 적용
    ### 5. conn.close()으로 디비연결 종료

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

    @staticmethod
    def select(where_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')
        try:
            with conn.cursor() as cur:

                # 들어오는 명렁어가 None, "all"이 아니라면 where과 이후를 추가 해서 검색
                # 들어오는 명령어가 None, "all"이라면 테이블 전체를 검색 
                add_query = ""
                if (where_data is not None) and (where_data != "all"):
                    add_query = " WHERE "
                    add_query += where_data

                # 검색, 결과도출
                ## 추후 가공을 고려하여 좀더 편하게 하기위해서 pd를 사용하여 dataframe형으로 반환
                query = "SELECT * FROM mytable" + add_query + ";"
                result_query = pd.read_sql(query, con = conn)
                
                # 전송을 위해 dataframe -> dict으로 변환
                result_query = result_query.to_dict('records')  # 형식: {time, plant..}, {time, plant...}
                # 받고나서 다시 dict -> dataframe로 변환 [df = pd.DataFrame(df)]

                ''' ex) WHERE
                plant='hub' // 식물이 허븬거 찾기
                plant LIKE 'temp%' // temp*인거 모두 ex) temp_plan, temp_abcdf...
                time BETWEEN '2021-06-22 14:00:00' AND '2021-06-22 14:40:00' // ~부터 ~까지 
                temperature < 7
                '''

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def delete(delete_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')
        try:
            with conn.cursor() as cur:

                # where 이후 문자열을 받아서 다바애 적용
                add_query = delete_data
                query = "DELETE FROM mytable WHERE " + add_query + ";"
                cur.execute(query)

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def db_limite(limite_count):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')
        try:
            with conn.cursor() as cur:

                # 테이블의 전체 row 갯수를 반환
                query = "select count(*) as cnt from mytable;"
                cur.execute(query)
                conn.commit()

                # row 갯수 반환값이 이중 튜플이기 때문에 int로 변환작업
                row_count = list(cur.fetchall())
                row_count = list(row_count[0])
                row_count = int(row_count[0])

                # 제한 행 수랑 현제 행 수를 비교하여 delete_count에 삭제할 행 수를 저장
                delete_count = 0
                if row_count > limite_count:
                    delete_count = row_count - limite_count

                # 삭제할 수만큼 반복
                ### 쿼리시 min(time) + n 이 작동하지 않아서 min(time)으로 삭제한 후에
                ### commit()을 하여 자동으로 min(time)이 바뀌는것을 이용해서 삭제
                for i in range(0, delete_count):
                    query = "DELETE FROM mytable WHERE time in(SELECT min(time) FROM mytable);"
                    cur.execute(query)
                    conn.commit()

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def insert_test(test_n):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')
        try:
            with conn.cursor() as cur:

                # 전달받은 int 값만큼 반복해서 테이블에 행 추가
                # 2000-01-22 11:22:xx - xx부분만 바뀌는거라 max는 100이고 시간 안겹치게 조심
                for i in range(0, test_n):
                    query = "INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:" + str(i) + "', 'test_plan', 12, 34, 56.78);"
                    cur.execute(query)
                    conn.commit()

                conn.commit()
        finally:
            conn.close()

    # 미사용
    @staticmethod
    def update(update_data):
        '''
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')
        try:
            with conn.cursor() as cur:

                conn.commit()
        finally:
            conn.close()
        '''

# test space ----------------------------------------
''''''
