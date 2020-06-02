#-*-coding:UTF-8 -*-
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()
sql1 ='SELECT * FROM (SELECT * FROM 球員 LEFT JOIN 退休球員 USING (學號) LEFT JOIN 隊長 USING (學號)) t1 LEFT JOIN (SELECT 學號,COUNT(學號) as 出賽場次 FROM 球員比賽表現 GROUP BY 學號) t2 USING(學號);'
sql2 ='SELECT 球員比賽表現.學號, count(球員比賽表現.學號) as 上場次數, (sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1)/count(球員比賽表現.學號) as 得分率, sum(表現.進攻籃板)/count(球員比賽表現.學號) as 進攻籃板率, sum(表現.防守籃板)/count(球員比賽表現.學號) as 防守籃板率, sum(表現.助攻)/count(球員比賽表現.學號) as 助攻率, sum(表現.阻攻)/count(球員比賽表現.學號) as 阻攻率, sum(表現.抄截)/count(球員比賽表現.學號) as 抄截率, sum(表現.犯規)/count(球員比賽表現.學號) as 犯規率, sum(表現.失誤)/count(球員比賽表現.學號) as 失誤率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號'
sql3 ='SELECT 球員比賽表現.學號, (sum(表現.三分球中)/sum(表現.三分球投)*100) as 三分球命中率, ((sum(表現.三分球中)+sum(表現.二分球中))/(sum(表現.三分球投)+sum(表現.二分球投))*100) as 投球命中率, (sum(表現.罰球中)/sum(表現.罰球投)*100) as 罰球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號;'
sql4 = "SELECT * FROM (SELECT 球員比賽表現.日期,(sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1) as 我方得分 FROM 球員比賽表現 LEFT JOIN 表現 USING(編號) GROUP BY 球員比賽表現.日期) t1 LEFT JOIN (SELECT * FROM 比賽) t2 USING(日期);"
sql5 ='SELECT (round(cast(sum(二分球中*2)+sum(三分球中*3)+sum(罰球中)as float)))/count(DISTINCT 日期) as 平均得分, (round(cast(sum(防守籃板)+sum(進攻籃板)as float)))/count(DISTINCT 日期) as 籃板平均, round(cast(sum(助攻)as float))/count(DISTINCT 日期) as 助攻平均, round(cast(sum(阻攻)as float))/count(DISTINCT 日期) as 阻攻平均, round(cast(sum(抄截)as float))/count(DISTINCT 日期) as 抄截平均, round(cast(sum(犯規)as float))/count(DISTINCT 日期) as 犯規平均, round(cast(sum(失誤)as float))/count(DISTINCT 日期) as 失誤平均 FROM 球員比賽表現 LEFT JOIN 表現 ON 表現.編號=球員比賽表現.編號;'
sql6 ='SELECT sum(二分球中)/sum(二分球投) as 二分命中率, sum(三分球中)/sum(三分球投) as 三分命中率, sum(罰球中)/sum(罰球投) as 罰球命中率 FROM 表現;'
sql7 ='SELECT 球員比賽表現.學號, (sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1) as 得分 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 得分 DESC;'
sql8 ='SELECT 球員比賽表現.學號, (sum(表現.防守籃板) + sum(表現.進攻籃板)) as 籃板 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 籃板 DESC;'
sql9 ='SELECT 球員比賽表現.學號, sum(表現.助攻) as 助攻 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 助攻 DESC;'
sql10='SELECT 球員比賽表現.學號, sum(表現.阻攻) as 阻攻 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 阻攻 DESC;'
sql11='SELECT 球員比賽表現.學號, sum(表現.抄截) as 抄截 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 抄截 DESC;'
sql12='SELECT 球員比賽表現.學號, (sum(表現.三分球中)/sum(表現.三分球投)*100) as 三分球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 三分球命中率 DESC;'
sql13='SELECT 球員比賽表現.學號, ((sum(表現.三分球中)+sum(表現.二分球中))/(sum(表現.三分球投)+sum(表現.二分球投))*100) as 投球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 投球命中率 DESC;'
sql14='SELECT 球員比賽表現.學號, (sum(表現.罰球中)/sum(表現.罰球投)*100) as 罰球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 罰球命中率 DESC;'

sql15='SELECT * FROM 球員比賽表現 LEFT JOIN 球員 USING(學號) LEFT JOIN 表現 USING(編號) WHERE 日期=%s and 盃賽名稱=%s and 對手學校=%s and 對手系名=%s;'
# sql16='SELECT 學號,背號 FROM 球員 LEFT JOIN 退休球員 USING(學號) where 退休學年 is NULL'

def player_info(sql1):
    try:
        cursor.execute(sql1)
        data = cursor.fetchall()
        print ("sql1: ")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            d3 = row[3]
            d4 = row[4]
            d5 = row[5]
            d6 = row[6]
            if (d4 == None):
                d4='0'
            if (d5 == None):
                d5=0
            if (d6 == None):
                d6=0
            print ("d0=%s,d1=%s,d2=%d,d3=%s,d4=%s,d5=%d,d6=%d" %(d0,d1,d2,d3,d4,d5,d6))
    except:
        print ("sql1 error")

def player_data_average(sql2):
    try:
        cursor.execute(sql2)
        data = cursor.fetchall()
        print ("sql2:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            d3 = row[3]
            d4 = row[4]
            d5 = row[5]
            d6 = row[6]
            d7 = row[7]
            d8 = row[8]
            d9 = row[9]
            print ("d0=%s,d1=%d,d2=%.2f,d3=%.2f,d4=%.2f,d5=%.2f,d6=%.2f,d7=%.2f,d8=%.2f,d9=%.2f" %(d0,d1, d2, d3, d4,d5,d6,d7,d8,d9))
    except:
        print ("sql2 error")

def player_hit_rate(sql3):
    try:
        cursor.execute(sql3)
        data = cursor.fetchall()
        print ("sql3:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            d3 = row[3]
            if (d1 == None):
                d1=0
            if (d2 == None):
                d2=0
            if (d3 == None):
                d3=0
            print ("d0=%s,d1=%d,d2=%d,d3=%d" %(d0, d1, d2, d3 ))
    except:
        print ("sql3 error")

def game_score(sql4):
    try:
        cursor.execute(sql4)
        data = cursor.fetchall()
        print ("sql4:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            d3 = row[3]
            d4 = row[4]
            d5 = row[5]
            print ("d0=%s,d2=%s,d3=%s,d4=%s,d1=%d,d5=%d" %(d0, d2, d3, d4, d1,d5))
    except:
        print ("sql4 error")

def data_average(sql5):
    try:
        cursor.execute(sql5)
        data = cursor.fetchall()
        print ("sql5:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            d3 = row[3]
            d4 = row[4]
            d5 = row[5]
            print ("d0=%.2f,d1=%.2f,d2=%f,d3=%.2f,d4=%.2f,d5=%.2f" %(d0, d1, d2, d3, d4, d5 ))
    except:
        print ("sql5 error")

def team_hit_rate(sql6):
    try:
        cursor.execute(sql6)
        data = cursor.fetchall()
        print ("sql6:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            d2 = row[2]
            print ("d0=%.2f,d1=%.2f,d2=%.2f" %(d0, d1, d2))
    except:
        print ("sql6 error")

def score_mvp(sql7):
    try:
        cursor.execute(sql7)
        data = cursor.fetchall()
        print ("sql7:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            print ("d0=%s,d1=%d" %(d0,d1))
    except:
        print ("sql7 error")

def backboard_mvp(sql8):
    try:
        cursor.execute(sql8)
        data = cursor.fetchall()
        print ("sql8:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            print ("d0=%s,d1=%d" %(d0,d1))
    except:
        print ("sql8 error")

def assist_mvp(sql9):
    try:
        cursor.execute(sql9)
        data = cursor.fetchall()
        print ("sql9:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            print ("d0=%s,d1=%d" %(d0,d1))
    except:
        print ("sql9 error")
        
def block_mvp(sql10):
    try:
        cursor.execute(sql10)
        data = cursor.fetchall()
        print ("sql10:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            print ("d0=%s,d1=%d" %(d0,d1))
    except:
        print ("sql10 error")

def intercept_mvp(sql11):
    try:
        cursor.execute(sql11)
        data = cursor.fetchall()
        print ("sql11:")
        print (data)
        for row in data:
            d0 = row[0]
            d1 = row[1]
            print ("d0=%s,d1=%d" %(d0,d1))
    except:
        print ("sql11 error")

def three_point_rate(sql12):
    try:
        cursor.execute(sql12)
        data = cursor.fetchall()
        print ("sql12:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            if(d1 == None):
                d1=0
            print ("d0=%s,d1=%.2f" %(d0,d1))
    except:
        print ("sql12 error")

def shoot_rate_mvp(sql13):
    try:
        cursor.execute(sql13)
        data = cursor.fetchall()
        print ("sql13:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            if(d1 == None):
                d1=0
            print ("d0=%s,d1=%.2f" %(d0,d1))
    except:
        print ("sql13 error")

def penalty_mvp(sql14):
    try:
        cursor.execute(sql14)
        data = cursor.fetchall()
        print ("sql14:")
        for row in data:
            d0 = row[0]
            d1 = row[1]
            if (d1 == None):
                d1=0
            print ("d0=%s,d1=%.2f" %(d0,d1))
    except:
        print ("sql14 error")

def show_record(sql15,date,game_name,competitor_school,competitor_dept_name):#有條件輸入
    try:
        cursor.execute(sql15, (date,game_name,competitor_school,competitor_dept_name))
        data = cursor.fetchall()
        print ("sql15:")
        print (data)
        # for row in data:
        #     d0 = row[0]
        #     d1 = row[1]
        #     d2 = row[2]
        #     d3 = row[3]
        #     d4 = row[4]
        #     d5 = row[5]
        #     d6 = row[6]
        #     d7 = row[7]
        #     d8 = row[8]
        #     d9 = row[9]
        #     d10 = row[10]
        #     d11 = row[11]
        #     d12 = row[12]
        #     d13 = row[13]
        #     d14 = row[14]
        #     d15 = row[15]
        #     d16 = row[16]
        #     d17 = row[17]
        #     d18 = row[18]
        #     d19 = row[19]
        #     d20 = row[20]
        #     d21 = row[21]
        #     d22 = row[22]
        #     print ("%d,%s,%s,%s,%s,%s,%s,%d,%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d" %(d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22))
    except:
        print ("sql15 error")

def online_player():
    sql16 = 'SELECT 學號,背號 FROM 球員 LEFT JOIN 退休球員 USING(學號) WHERE 退休學年 is NULL'
    try:
        cursor.execute(sql16)
        data = cursor.fetchall()
        return data
    except:
        return None

# player_info(sql1)
# player_data_average(sql2)
# player_hit_rate(sql3)
# game_score(sql4)
# data_average(sql5)
# team_hit_rate(sql6)
# score_mvp(sql7)
# backboard_mvp(sql8)
# assist_mvp(sql9)
# block_mvp(sql10)
# intercept_mvp(sql11)
# three_point_rate(sql12)
# shoot_rate_mvp(sql13)
# penalty_mvp(sql14)
# #show_record(sql15) 有條件輸入
# online_player()

# conn.close()

# connent close 的話呼叫會斷掉 資料沒辦法回傳
# sql指令要放在函式裡面，因為從main_board呼叫的時候沒辦法傳入
# server不用print任何東西，要是失敗的話就回傳 None
