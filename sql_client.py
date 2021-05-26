import pymysql

class sql_client:
    
    def first():
        # 포트 : 디폴트 3306
        conn = pymysql.connect(host='localhost', user='root', password='password',
        db = 'mysql', charset='utf8')
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