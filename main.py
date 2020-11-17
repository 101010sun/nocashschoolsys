from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import server
import os

app = Flask(__name__)
# open debugger
app.config['DEBUG'] = True
app.config['MONGO_DBNAME'] = 'nocashschoolsys'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/nocashschoolsys'
app.config['SECRET_KEY'] = os.urandom(24)

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('login.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        student = mongo.db.student
        teacher = mongo.db.teacher
        nid = request.form['NID'].upper()
        isstudent = student.find_one({'NID': nid})
        isteacher = teacher.find_one({'NID': nid})
        if isstudent is not None or isteacher is not None:
            session['username'] = nid
            return redirect(url_for('index'))
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        student = mongo.db.student
        teacher = mongo.db.teacher
        nid = request.form['NID'].upper()
        isstudent = student.find_one({'NID': nid})
        isteacher = teacher.find_one({'NID': nid})
        if isstudent is None and 'D' in nid:
            session['username'] = nid
            return render_template('register_student.html')
        elif isteacher is None and 'T' in nid:
            session['username'] = nid
            return render_template('register_teacher.html')
        return 'That NID already exists!'

    return render_template('register.html')

@app.route('/register/student', methods=['Get', 'POST'])
def register_student():
    


if __name__ == "__main__":
    app.run(host ='127.0.0.1')