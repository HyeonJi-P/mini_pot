import pymysql

def test():
    conn = pymysql.connect(host='localhost', port=3306, user='auint', password='*6CC6A1C22CFFA93B23769CAE343636557E024D12',
    db = 'mysql', charset='utf8')
    cur = conn.cursor()

    sql = "SELECT*FROM mytable"
    cur.execute(sql)
    conn.commit()

    #sql = "INSERT INTO mytable(time, plant, temperature, humidity, illuminance) VALUES('2021-06-22 14:48:11.003', 'temp_plan', 6, 7, 8.88);"
    #cur.execute(sql)
    #conn.commit()

    #rows = cur.fetchall()
    #print(rows)


    conn.close()


test()



