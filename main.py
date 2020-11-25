from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import server
import os
import time

app = Flask(__name__)
# open debugger
app.config['DEBUG'] = True
app.config['MONGO_DBNAME'] = 'nocashschoolsys'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/nocashschoolsys'
app.config['SECRET_KEY'] = os.urandom(24)

mongo = PyMongo(app)

@app.route('/', methods=['GET','POST'])
def index():
    if 'username' in session:
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout', methods=['GET','POST'])
def logout():
    if request.method == 'POST':
        session['username'] =  False
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
            return render_template('home_page.html', nid = nid)
        return render_template('login.html')
    return redirect(url_for('index'))

@app.route('/home_page', methods=['GET','POST'])
def home_page():
    nid = session.get('username')
    if request.method == 'POST':
        if nid is not None: 
            return render_template('home_page.html', nid = nid)
        return render_template('longin')
    return render_template('home_page.html', nid = nid)

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
            return redirect(url_for('register_student'))
        elif isteacher is None and 'T' in nid:
            session['username'] = nid
            return redirect(url_for('register_teacher'))
        return 'That NID already exists!'

    return render_template('register.html')

@app.route('/register/student', methods=['Get', 'POST'])
def register_student():
    if request.method == 'POST':
        nid = session.get('username')
        if nid is not None and 'D' in nid:
            server.insert_student(nid, request.form['Name'], request.form['Dept'], int(request.form['Grade']), request.form['Sex'], request.form['Residence'])
            server.create_moneybag(nid) #create bag
            data = time.strftime("%Y-%m-%d",time.localtime()) #format time
            server.insert_money("None", nid, "None",  data, 10, 1)
            return redirect(url_for('index'))
        return render_template('register_student.html')
    return render_template('register_student.html')

@app.route('/register/teacher', methods=['Get', 'POST'])
def register_teacher():
    if request.method == 'POST':
        nid = session.get('username')
        if nid is not None and 'T' in nid:
            server.insert_teacher(nid, request.form['Name'], request.form['Dept'])
            server.insert_temoney(nid)
            return redirect(url_for('index'))
        return render_template('register_teacher.html')
    return render_template('register_teacher.html')

@app.route('/activity', methods=['Get', 'POST'])
def activity():
    nid = session.get('username')
    if nid is not None and 'T' in nid:
        return redirect(url_for('activity_teacher'))
    elif nid is not None and 'D' in nid:
        return redirect(url_for('activity_student'))
    return render_template('home_page.html', nid = nid)


@app.route('/activity_teacher', methods=['Get', 'POST'])
def activity_teacher():
    if request.method == 'POST':
        nid = session.get('username')
        if nid is not None:
            server.insert_active(request.form['ActiveName'], int(request.form['Credit']))
            return render_template('activity_teacher.html')
        return redirect(url_for('login'))
    return render_template('activity_teacher.html')

@app.route('/activity_student', methods=['Get', 'POST'])
def activity_student():
    if request.method == 'POST':
        nid = session.get('username')
        if nid is not None:
            return render_template('activity_student.html')
        return redirect(url_for('login'))
    return render_template('activity_student.html')

@app.route('/moneybag', methods=['Get','POST'])
def moneybag():
    nid = session.get('username')
    if nid is not None and 'T' in nid:
        return redirect(url_for('moneybag_teacher'))
    elif nid is not None and 'D' in nid:
        return redirect(url_for('moneybag_student'))   
    return render_template('home_page.html', nid = nid)

@app.route('/moneybag_student', methods=['Get','POST'])
def moneybag_student():
    nid = session.get('username')
    if nid is not None: 
        money = server.find_money(nid)
        return render_template('moneybag_student.html', nid = nid, money = money)
    return redirect(url_for('login'))

@app.route('/moneybag_teacher', methods=['Get','POST'])
def moneybag_teacher():
    nid = session.get('username')
    if nid is not None: 
        money = server.find_money(nid)
        return render_template('moneybag_teacher.html', nid = nid, money = money)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host ='127.0.0.1')