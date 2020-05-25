import pymysql

conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()
sql = "SELECT * FROM 比賽 WHERE 對手得分=16"
try:
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        d1 = row[0]
        d2 = row[1]
        d3 = row[2]
        d4 = row[3]
        d5 = row[4]
    print ("d1=%s,d2=%s,d3=%s,d4=%sd5=%s" % (d1, d2, d3, d4, d5))
except:
    print ("Error: unable to fetch data")
conn.close()
