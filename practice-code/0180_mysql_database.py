# pip install pymysql

import pymysql


mysql_conn = pymysql.connect(host='host_name', user='db_user', password='db_pass', database='db_name')

with mysql_conn.cursor() as cur:
    try:
        cur.execute("INSERT INTO key_table(key_name, key_value) VALUES (%s, %s)", ('a', 1))
        mysql_conn.commit()
    except Exception as e: print(f'Error: {e}')