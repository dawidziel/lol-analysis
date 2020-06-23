import sqlite3
conn = sqlite3.connect('API_sql.db')
cur = conn.cursor()
siwas = "k3w1s"
cur.execute('''insert into summ_list(summ_name) values(?)''', (siwas,))
print(cur.fetchall())
cur.execute('select * from summ_list')
print(cur.fetchall())
conn.commit()