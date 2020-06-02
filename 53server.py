#-*-coding:UTF-8 -*-
import pymysql

sql=' '
conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()