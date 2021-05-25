import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='*6CC6A1C22CFFA93B23769CAE343636557E024D12',
db = 'mysql', charset='utf8')

try:
    # cur = conn.cursor()
    with conn.cursor() as cur:
        
        # 이거이제 dict형으로 변환해줘야함.. 일단자고일ㄷ어나서
        sql = "INSERT INTO mytable(time,plant,temperature,humidity,illuminance) VALUSE (111, '222', 333, 444, 55.5)"
        cur.execute(sql)
        conn.commit()

        time DATETIME NOT NULL,
        plant varchar(20) NULL,
        temperature int NULL,
        humidity int NULL,
        illuminance float NULL,

        cur.execute("SELECT* FROM mytable")
        rows = cur.fetchall()
        print(rows)

finally:
    conn.close()
