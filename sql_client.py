import pymysql

class sql_client:
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='*6CC6A1C22CFFA93B23769CAE343636557E024D12', 
        db = 'mysql', charset='utf8')

        try:
            # cur = conn.cursor()
            with conn.cursor() as cur:

                col = ','.join(insert_data.keys())
                val = ','.join(insert_data.values())
                sql = "INSERT INTO mytable(%s) VALUSE(%s);" %(col, val)
                cur.execute(sql, insert_data.values())
                conn.commit()

        finally:
            conn.close()
