from pymongo import MongoClient
from bson.objectid import ObjectId
import time
#local host
conn = MongoClient()
#database
db = conn.nocashschoolsys
#collection
col_active       = db.active
col_chooseactive = db.chooseactive
col_moneybag     = db.moneybag
col_moneyhistory = db.moneyhistory
col_student      = db.student
col_teacher      = db.teacher
#connect error or not
col_active.stats
col_chooseactive.stats
col_moneybag.stats
col_moneyhistory.stats
col_student.stats
col_teacher.stats
# insert
def insert_teacher(nid, name, dept):
    data = {'NID': nid, 'Name': name, 'Dept': dept}
    col_teacher.insert_one(data)

def insert_student(nid, name, dept, grade, sex, residence):
    data = {'NID': nid, 'Name': name, 'Dept': dept, 'Grade': grade, 'Sex': sex, 'Residence': residence}
    col_student.insert_one(data)

def insert_active(activename, tnid, credit):
    data = {'ActiveName': str(activename), 'TNID': str(tnid), 'Credit': int(credit)}
    col_active.insert_one(data)

def choose_active(nid,tnid,aid):
    data = {'NID': str(nid), 'TNID': str(tnid), 'AID': str(aid)}
    col_chooseactive.insert_one(data)

def create_moneybag(nid):
    data = {'NID': nid, 'Money': int(0)}
    col_moneybag.insert_one(data)

def insert_money(tnid,snid,anid,data,get,reason):
    data = {'TNID': str(tnid), 'SNID': str(snid),'ANID': str(anid), 'Data': str(data), 'Get': int(get), 'Reason': int(reason)}
    col_moneyhistory.insert_one(data) #add history
    update_money(tnid, int(get)*-1) #cut money from teacher's moneybag
    update_money(snid, int(get)) #student's moneybag add money
def insert_money2(snid,data,get,reason):
    data = {'SNID': str(snid), 'Data': str(data), 'Get': int(get), 'Reason': int(reason)}
    col_moneyhistory.insert_one(data)
    update_money(snid, int(get)) #student's moneybag add money
def insert_money3(tnid,data,get,reason):
    data = {'TNID': str(tnid), 'Data': str(data), 'Get': int(get), 'Reason': int(reason)}
    col_moneyhistory.insert_one(data)
    update_money(tnid, int(get)) #student's moneybag add money

# find
def find_teacher():
    cursor = col_teacher.find({})
    data = [d for d in cursor]
    return(data)

def find_student():
    cursor = col_student.find({})
    data = [d for d in cursor]
    return(data)

def find_active():
    cursor = col_active.find({})
    data = [d for d in cursor]
    return(data)
def find_teactive(tnid):
    cursor = col_active.find({"TNID": str(tnid)})
    data = [d for d in cursor]
    return(data)

def find_stchooseactive(nid):
    cursor = col_chooseactive.find({"NID":str(nid)})
    data = [d for d in cursor]
    return(data)

def find_techooseactive(nid,aid):
    cursor = col_chooseactive.find({"TNID":str(nid), "AID":str(aid)})
    data = [d for d in cursor]
    return(data)

def find_stmoneyhistory(snid):
    cursor = col_moneyhistory.find({"SNID": str(snid)})
    data = list()
    for d in cursor:
        data.append(d)
        if d['Reason'] == 1: d['Reason'] = str('註冊')
        elif d['Reason'] == 2: d['Reason'] = str('點名')
        elif d['Reason'] == 3: d['Reason'] = str('課程互動')
        elif d['Reason'] == 4: d['Reason'] = str('準時交作業')
        elif d['Reason'] == 5: d['Reason'] = str('期中期末考試成績優異')
        else: d['Reason'] = str('小考成績優異')
    return(data)
def find_temoneyhistory(tnid):
    cursor = col_moneyhistory.find({"TNID": str(tnid)})
    data = list()
    for d in cursor:
        data.append(d)
        if d['Reason'] == 1: d['Reason'] = str('註冊')
        elif d['Reason'] == 2: d['Reason'] = str('點名')
        elif d['Reason'] == 3: d['Reason'] = str('課程互動')
        elif d['Reason'] == 4: d['Reason'] = str('準時交作業')
        elif d['Reason'] == 5: d['Reason'] = str('期中期末考試成績優異')
        else: d['Reason'] = str('小考成績優異')
    return(data)

def find_money(nid):
    cursor = col_moneybag.find_one({'NID': nid})
    return(int(cursor['Money']))
def update_money(nid,get):
    money = int(find_money(nid))
    col_moneybag.update_one(filter={'NID': nid}, update={'$inc': {'Money':get}})

def find_chooseactive():
    cursor = col_chooseactive.find({})
    data = [d for d in cursor]
    return(data)

def find_moneybag():
    cursor = col_moneybag.find({})
    data = [d for d in cursor]
    return(data)

def find_moneyhistory():
    cursor = col_moneyhistory.find({})
    data = [d for d in cursor]
    return(data)

