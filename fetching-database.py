import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='sambal_bakar'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM penjualan")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
cursor.close()
conn.close()