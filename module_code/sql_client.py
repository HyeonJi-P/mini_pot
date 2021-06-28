import pymysql

class sql_client:
    def insert(insert_data):
        conn = pymysql.connect(host='localhost', port=3306, user='auint', password='', 
        db = 'mysql', charset='utf8')

        try:
            with conn.cursor() as cur:

                

                
                cur.execute()
                conn.commit()

        finally:
            conn.close()
