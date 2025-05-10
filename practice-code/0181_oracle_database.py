# pip install cx_oracle

import cx_Oracle

oracle_conn = cx_Oracle.connect(user='db_user', password='db_pass', dsn=f"{'host_name'}/{'db_name'}")