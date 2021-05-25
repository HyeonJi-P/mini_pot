import pymysql

# 포트 : 디폴트 3306
conn = pymysql.connect(host='localhost', user='root', password='*6CC6A1C22CFFA93B23769CAE343636557E024D12', charset='utf8')
cur = conn.cursor()

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
