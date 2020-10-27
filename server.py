from pymongo import MongoClient
from bson.objectid import ObjectId

#local host
conn = MongoClient()
#database
db = conn.nocashschoolsys
#collection
col_active = db.active
col_organization = db.organization
col_student = db.student
col_teacher = db.teacher
#connect error or not
col_active.stats
col_organization.stats
col_student.stats
col_teacher.stats
# insert
def insert_teacher(nid, name, dept):
    data = {'NID': nid, 'Name': name, 'Dept': dept}
    col_teacher.insert_one(data)

def insert_student(nid, name, dept, grade, sex, residence):
    data = {'NID': nid, 'Name': name, 'Dept': dept, 'Grade': grade, 'Sex': sex, 'Residence': residence}
    col_student.insert_one(data)

def insert_organization(nid, organname):
    data = {'NID': nid, 'OrganName': organname}
    col_organization.insert_one(data)

def insert_active(activename, average, credit, rank):
    data = {'ActiveName': activename, 'Average': average, 'Credit': credit, 'Rank': rank}
    col_active.insert_one({'ActiveName': activename, 'Average': average, 'Credit': credit, 'Rank': rank})
# find
def find_teacher():
    cursor = col_teacher.find({})
    data = [d for d in cursor]
    print(data)

def find_student():
    cursor = col_student.find({})
    data = [d for d in cursor]
    print(data)

def find_active():
    cursor = col_active.find({})
    data = [d for d in cursor]
    print(data)

def find_organization():
    cursor = col_organization.find({})
    data = [d for d in cursor]
    print(data)
