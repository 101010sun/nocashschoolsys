from flask import Flask, render_template
import flask_pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)
# open debugger
app.config['DEBUG'] = True
#connect to nocashschoolsys db
mongo = PyMongo(app, uri="mongodb://localhost:27017/nocashschoolsys")
#find the person by NID
@app.route('/user/<string:NID>')
def query_user(NID):
    if NID:
        users = mongo.db.student.find({'NID': NID})
        print(users)
        if users: 
            return 
        else: 
            return 'No user found!'
#homepage
@app.route("/")
def main():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host ='127.0.0.1')