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
        d0 = row[0]
        d1 = row[1]
        d2 = row[2]
        d3 = row[3]
        d4 = row[4]
    print ("d0=%s,d1=%s,d2=%s,d3=%sd4=%s" % (d0, d1, d2, d3, d4))
except:
    print ("Error: unable to fetch data")
conn.close()
