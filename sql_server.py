import pymysql
import json
import pandas as pd

# 완-insert : dict형을 받아서 디비에 저장해준다.
'''사용자가 직접 col을 추가한다는 상황은? <== 그럼 사용자가 삽입삭제수정 다 할 수 있게 해야하긴 한데... 흠... '''

# 완-select : SQLquery문의 where이후 문자열을 받아서 조회한다.
'''인덱스로 접근하여 처리하는법'''

# 완-delete : WHERE 이후 문자열을 받아 삭제한다.
    # 미-db_limite : 라즈베리파이 같은경우 임시 저장소니까 갯수제한을 둬서 행을 삭제 (순서대로-예전데이터)

# 널-updata : 수정할때는 없는거 같음 아마..?


class sql_server:

    @staticmethod
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')  # *6CC6A1C22CFFA93B23769CAE343636557E024D12

        try:
            # cur = conn.cursor()랑 같은 의미
            with conn.cursor() as cur:

                # DB에 쿼리로 데이터 추가
                col_list = list(insert_data.keys())
                col = ', '.join(col_list)

                #val = ','.join(map(str, insert_data.values())) <== 이렇게하면 문자열이 ''로 안둘려서 나옴
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

                query = "INSERT INTO mytable(%s) VALUES(%s);" %(col, val)
                cur.execute(query)  # cur.execute(query, insert_data.values())

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def select(where_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                # 들어오는 명렁어 추가 해서 검색하기 
                add_query = ""
                if (where_data is not None) and (where_data != "all"):
                    add_query = " WHERE "
                    add_query += where_data

                # 검색, 결과도출 
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

                add_query = delete_data
                query = "DELETE FROM mytable WHERE " + add_query + ";"
                cur.execute(query)

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def update(update_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                conn.commit()
        finally:
            conn.close()

    @staticmethod
    def db_limite():
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                query = "select count(*) as cnt from mytable;"
                cur.execute(query)
                conn.commit()

                temp = list(cur.fetchall())
                print(temp)

                print(type(result))
                print(result)

                '''
                limite_count = 10

                for i in range(0, limite_count):
                    query = "DELETE FROM mytable WHERE time in(SELECT min(time) FROM mytable);"
                    cur.execute(query)
                    conn.commit()
                '''




                conn.commit()
        finally:
            conn.close()


#------------------------------------
# now test
'''
dict_message = {
    'time' : '2000-11-22 11:22:33',
    'plant' : 'baechu',
    'temperature': 21,
    'humidity': 6,
    'illuminance': 24.13
}

#sql_server.insert(dict_message)
#print("----------1")

#sql_server.select(None)
#print("----------2")

#sql_server.select("all")
#print("----------3")

tempp = "plant = 'hub'"
sql_server.select(tempp)
print("----------4")
'''
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:01', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:02', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:03', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:04', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:05', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:06', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:07', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:08', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:09', 'plan?', 1, 2, 3.45);
#INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2000-01-22 11:22:10', 'plan?', 1, 2, 3.45);

#time in(select min(time) from mytable);
#select min(time) from mytable;

#DELETE FROM mytable WHERE time in(SELECT min(time) FROM mytable);

#select count(*) as cnt from mytable; 카운트 

sql_server.db_limite()
 