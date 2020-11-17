from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import server
import bcrypt
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
        users = mongo.db.student
        login_user = users.find_one({'NID': request.form['NID']})
        if login_user is not None:
            session['username'] = request.form['NID']
            return redirect(url_for('index'))
        return ''
    return redirect(url_for('index'))

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.student
        existing_user = users.find_one({'NID': request.form['NID']})

        if existing_user is None:
            server.insert_student(request.form['NID'], request.form['Name'], request.form['Dept'], int(request.form['Grade']), float(request.form['Average']), int(request.form['Rank']), request.form['Sex'], request.form['Residence'])
            session['username'] = request.form['NID']
            return redirect(url_for('index'))

        return 'That NID already exists!'

    return render_template('register.html')


if __name__ == "__main__":
    app.run(host ='127.0.0.1')