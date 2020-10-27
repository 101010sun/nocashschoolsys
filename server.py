from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient()
db = conn.nocashschoolsys
col_teacher = db.teacher

col_teacher.stats

cursor = col_teacher.find({})

data = [d for d in cursor]
print(data)