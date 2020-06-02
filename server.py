#-*-coding:UTF-8 -*-
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='yuan',
    password='test1234',
    database='testdb'
)
cursor = conn.cursor()

def player_info(sql1):
    try:
        cursor.execute(sql1)
        data = cursor.fetchall()
        return data
    except:
        return None

def player_data_average():
    sql2 ='SELECT 球員比賽表現.學號, count(球員比賽表現.學號) as 上場次數, (sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1)/count(球員比賽表現.學號) as 得分率, sum(表現.進攻籃板)/count(球員比賽表現.學號) as 進攻籃板率, sum(表現.防守籃板)/count(球員比賽表現.學號) as 防守籃板率, sum(表現.助攻)/count(球員比賽表現.學號) as 助攻率, sum(表現.阻攻)/count(球員比賽表現.學號) as 阻攻率, sum(表現.抄截)/count(球員比賽表現.學號) as 抄截率, sum(表現.犯規)/count(球員比賽表現.學號) as 犯規率, sum(表現.失誤)/count(球員比賽表現.學號) as 失誤率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號'
    try:
        cursor.execute(sql2)
        data = cursor.fetchall()
        return data
    except:
        return None

def player_hit_rate():
    sql3 ='SELECT 球員比賽表現.學號, (sum(表現.三分球中)/sum(表現.三分球投)*100) as 三分球命中率, ((sum(表現.三分球中)+sum(表現.二分球中))/(sum(表現.三分球投)+sum(表現.二分球投))*100) as 投球命中率, (sum(表現.罰球中)/sum(表現.罰球投)*100) as 罰球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號;'
    try:
        cursor.execute(sql3)
        data = cursor.fetchall()
        return data
    except:
        return None

def game_score():
    sql4 = "SELECT * FROM (SELECT 球員比賽表現.日期,(sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1) as 我方得分 FROM 球員比賽表現 LEFT JOIN 表現 USING(編號) GROUP BY 球員比賽表現.日期) t1 LEFT JOIN (SELECT * FROM 比賽) t2 USING(日期);"
    try:
        cursor.execute(sql4)
        data = cursor.fetchall()
        return data
    except:
        return None

def data_average():
    sql5 ='SELECT (round(cast(sum(二分球中*2)+sum(三分球中*3)+sum(罰球中)as float)))/count(DISTINCT 日期) as 平均得分, (round(cast(sum(防守籃板)+sum(進攻籃板)as float)))/count(DISTINCT 日期) as 籃板平均, round(cast(sum(助攻)as float))/count(DISTINCT 日期) as 助攻平均, round(cast(sum(阻攻)as float))/count(DISTINCT 日期) as 阻攻平均, round(cast(sum(抄截)as float))/count(DISTINCT 日期) as 抄截平均, round(cast(sum(犯規)as float))/count(DISTINCT 日期) as 犯規平均, round(cast(sum(失誤)as float))/count(DISTINCT 日期) as 失誤平均 FROM 球員比賽表現 LEFT JOIN 表現 ON 表現.編號=球員比賽表現.編號;'
    try:
        cursor.execute(sql5)
        data = cursor.fetchall()
        return data
    except:
        return None

def team_hit_rate():
    sql6 ='SELECT sum(二分球中)/sum(二分球投) as 二分命中率, sum(三分球中)/sum(三分球投) as 三分命中率, sum(罰球中)/sum(罰球投) as 罰球命中率 FROM 表現;'
    try:
        cursor.execute(sql6)
        data = cursor.fetchall()
        return data
    except:
        return None

def score_mvp():
    sql7 ='SELECT 球員比賽表現.學號, (sum(表現.二分球中)*2 + sum(表現.三分球中)*3 + sum(表現.罰球中)*1) as 得分 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 得分 DESC;'
    try:
        cursor.execute(sql7)
        data = cursor.fetchall()
        return data
    except:
        return None

def backboard_mvp():
    sql8 ='SELECT 球員比賽表現.學號, (sum(表現.防守籃板) + sum(表現.進攻籃板)) as 籃板 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 籃板 DESC;'
    try:
        cursor.execute(sql8)
        data = cursor.fetchall()
        return data
    except:
        return None

def assist_mvp():
    sql9 ='SELECT 球員比賽表現.學號, sum(表現.助攻) as 助攻 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 助攻 DESC;'
    try:
        cursor.execute(sql9)
        data = cursor.fetchall()
        return data
    except:
        return None
        
def block_mvp():
    sql10='SELECT 球員比賽表現.學號, sum(表現.阻攻) as 阻攻 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 阻攻 DESC;'
    try:
        cursor.execute(sql10)
        data = cursor.fetchall()
        return data
    except:
        return None

def intercept_mvp():
    sql11='SELECT 球員比賽表現.學號, sum(表現.抄截) as 抄截 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 抄截 DESC;'
    try:
        cursor.execute(sql11)
        data = cursor.fetchall()
        return data
    except:
        return None

def three_point_rate():
    sql12='SELECT 球員比賽表現.學號, (sum(表現.三分球中)/sum(表現.三分球投)*100) as 三分球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 三分球命中率 DESC;'
    try:
        cursor.execute(sql12)
        data = cursor.fetchall()
        return data
    except:
        return None

def shoot_rate_mvp():
    sql13='SELECT 球員比賽表現.學號, ((sum(表現.三分球中)+sum(表現.二分球中))/(sum(表現.三分球投)+sum(表現.二分球投))*100) as 投球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 投球命中率 DESC;'
    try:
        cursor.execute(sql13)
        data = cursor.fetchall()
        return data
    except:
        return None

def penalty_mvp():
    sql14='SELECT 球員比賽表現.學號, (sum(表現.罰球中)/sum(表現.罰球投)*100) as 罰球命中率 FROM 球員比賽表現 LEFT JOIN 表現 ON 球員比賽表現.編號 = 表現.編號 GROUP BY 球員比賽表現.學號 ORDER BY 罰球命中率 DESC;'
    try:
        cursor.execute(sql14)
        data = cursor.fetchall()
        return data
    except:
        return None

def show_record(date,game_name,competitor_school,competitor_dept_name):#有條件輸入
    sql15='SELECT * FROM 球員比賽表現 LEFT JOIN 球員 USING(學號) LEFT JOIN 表現 USING(編號) WHERE 日期=%s and 盃賽名稱=%s and 對手學校=%s and 對手系名=%s;'
    try:
        cursor.execute(sql15, (date,game_name,competitor_school,competitor_dept_name))
        data = cursor.fetchall()
        return data
    except:
        return None

def online_player():
    sql16 = 'SELECT 學號,背號 FROM 球員 LEFT JOIN 退休球員 USING(學號) WHERE 退休學年 is NULL'
    try:
        cursor.execute(sql16)
        data = cursor.fetchall()
        return data
    except:
        return None
