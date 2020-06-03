#-*-coding:UTF-8 -*-
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()

def new_data():
    sql = "INSERT INTO 球員( 名字, 學號, 背號, 入隊學年 )VALUES('孫乙玲', 'D0782838', 10, '107')"
    try:
        cursor.execute(sql,())
    # 執行SQL语句
   # 提交到資料庫系統執行
        conn.commit()
        print("insert a record into temp")
    except:
   # 發生異常錯誤時回復
        conn.rollback()
    
new_data()