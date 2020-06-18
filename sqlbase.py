import sqlite3
conn = sqlite3.connect('API_sql.db')
cur = conn.cursor()
cur.execute("insert into summ_list values(NULL,'gazowana kawa')")
print(cur.fetchall())
cur.execute('select * from summ_list')
print(cur.fetchall())
conn.commit()