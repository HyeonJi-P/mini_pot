import pymysql

class sql_client:
    def test():
        db = pymysql.connect(host='localhost', user='root', password='password',
        db = 'mydb', charset='utf8')
        cur = db.cursor()

        cur.execute("SELECT*FROM mytable")
        rows = cur.fetchall()
        print(rows)
        db.close()
    
    # 가장 처음에만 실행 => 디비 생성
    def first():
        # 포트 : 디폴트 3306
        conn = pymysql.connect(host='localhost', user='root', password='password', charset='utf8')
        cur = conn.cursor()

        sql = "CREATE DATABASE mydb"
        cur.execute(sql)
        conn.commit()

        sql = '''CREATE TABLE mytable(
            time DATETIME NOT NULL,
            plant varchar(20) NULL,
            temperature int NULL,
            humidity int NULL,
            illuminance float NULL
            PRIMARY KEY (time)
            );
            '''
        cur.execute(sql)
        conn.commit()


        conn.close()



sql_client.first()