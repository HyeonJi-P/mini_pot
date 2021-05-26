import pymysql

class sql_server:
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='-----', 
        db = 'mysql', charset='utf8')

        try:
            # cur = conn.cursor()
            with conn.cursor() as cur:

                col = insert_data.keys()
                val = insert_data.values()
                sql = "INSERT INTO mytable(%s) VALUSE(%s)" %(.join(col), .join(val))
                cur.execute(sql, insert_data.values())
                conn.commit()

        finally:
            conn.close()
