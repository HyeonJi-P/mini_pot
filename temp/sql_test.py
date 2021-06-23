import pymysql
import json

def test():
    conn = pymysql.connect(host='localhost', port=3306, user='auint', password='pwpw',
    db = 'mysql', charset='utf8')
    cur = conn.cursor()

    '''데이터 추출 하는중'''
    query = "SELECT * FROM mytable;"
    cur.execute(query)
    result = list(cur.fetchall())  # 튜플 타입으로 반환해줌 수정가능하게 list로 변환
    conn.commit()

    for i into range(0, len(result)):  # len(result) == row수 만큼
        print("%d번째줄 "%(i), result[i])

        for j into range(0, len(result[i])):
            print("%d줄의 %d번째 "%(i, j), result[i][j])



    ''' 데이터 삽입 완료
    query = "INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2021-06-22 16:31:11.003', 'temp_plan', 6, 7, 8.88);"
    cur.execute(query)
    conn.commit()
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



