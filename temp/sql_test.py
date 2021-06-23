import pymysql
import json

def test():
    conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw',
    db = 'mysql', charset='utf8')
    cur = conn.cursor()

    '''데이터 추출 하는중'''
    # 모든 col이름 받아오기 
    query = "SELECT column_name FROM information_schema.columns WHERE table_schema='mysql' AND table_name='mytable';"
    cur.execute(query)
    col = list(cur.fetchall())
    conn.commit()

    clear_str = "()',"  # (tuple - list, tuple - str)변환과정에서 생기는 찌꺼기 처리하기 
    for i in range(0, len(col)):
        col[i] = str(col[i])
        col[i] = ''.join(_ for _ in col[i] if _ not in clear_str)
    
    print(col)  # test용

    
    query = "SELECT * FROM mytable;"
    cur.execute(query)
    result = list(cur.fetchall())  # 튜플 타입으로 반환해줌 수정가능하게 list로 변환
    conn.commit()

    print(result)

    '''
    for i in range(0, len(result)):  # row수 만큼 ex) [0 ... n] (time, plant, temperature, humidity, illuminance)
        print("%d번째줄 "%(i), result[i])

        for j in range(0, len(result[i])):  # 각 row의 갯수 만큼 [0]==time, [1]==plant, [2]==temperature, [3]==humidity, [4]==illuminance
            print("%d줄의 %d번째 "%(i, j), result[i][j])

            if (i == 0) and (j == 0):
                print("date time 나누기", result[i][j].year, result[i][j].month, result[i][j].day, result[i][j].hour, result[i][j].minute, result[i][j].second)  # .microsecond는 조금 이상함 일단 패스
    '''

    # 어차피 row의 모든 데이터가 필요할 테니까 select는 all, 테이블은 일단 하나니까 from mytable, 조건은 변경가능
    ''' ex) SELECT * FROM mytable WHERE
    plant='hub' // 식물이 허븬거 찾기
    plant LIKE 'temp%' // temp*인거 모두 ex) temp_plan, temp_abcdf...
    time BETWEEN '2021-06-22 14:00:00' AND '2021-06-22 14:40:00' // ~부터 ~까지 
    temperature < 7
    '''

    


    ''' 데이터 삽입 완료
    query = "INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2021-06-22 16:31:11.003', 'temp_plan', 6, 7, 8.88);"
    cur.execute(query)
    conn.commit()

    INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2021-06-23 10:53:11.999', 'hub', 9, 10, 11.11);
    '''

    conn.close()


test()

''' result 결과
(
(datetime.datetime(2021, 6, 22, 14, 25, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 14, 36, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 14, 48, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 16, 31, 11), 'temp_plan', 6, 7, 8.88)
)


list타입
[
(datetime.datetime(2021, 6, 22, 14, 25, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 14, 36, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 14, 48, 11), 'temp_plan', 6, 7, 8.88),
(datetime.datetime(2021, 6, 22, 16, 31, 11), 'temp_plan', 6, 7, 8.88)
]
'''



