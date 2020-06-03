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
    sql = "INSERT INTO 球員( 名字, 學號, 背號, 入隊學年 )VALUES(%s, %s, %s, %s)"
    try:
        cursor.execute(sql,())
    # 執行SQL语句
    # 提交到資料庫系統執行
        conn.commit()
        print("insert a record into temp")
    except:
   # 發生異常錯誤時回復
        conn.rollback()
    
def fix_data(新名字,新學號,新背號,新入隊學年,舊名字,舊學號,舊背號,舊入隊學年):
    sql = "UPDATE 球員 SET 名字 = %s, 學號= %s ,背號 = %s,入隊學年= %s WHERE 球員.名字 = %s and 球員.學號 = %s and 球員.背號 = %s and 球員.入隊學年=%s "
    try:
        cursor.execute(sql,("新名字","新學號","新背號","新入隊學年","舊名字","舊學號","舊背號","舊入隊學年"))
    # 執行SQL语句
    # 提交到資料庫系統執行
        conn.commit()
        print("insert a record into temp")
    except:
   # 發生異常錯誤時回復
        conn.rollback()

fix_data()

