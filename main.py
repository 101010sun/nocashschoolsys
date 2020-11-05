# render_template :樣式模板使用 HTML 撰寫，後台處理使用 Python
# server.py       :連接資料庫
# request         :request請求來與HTML互動
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import server
import bcrypt

app = Flask(__name__)
# open debugger
app.config['DEBUG'] = True
app.config['MONGO_DBNAME'] = 'nocashschoolsys'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/nocashschoolsys'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'NID' in session:
        return 'You are logged in as ' + session['NID']
    return render_template('Home_page.html')

#login
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.student
    login_user = users.find_one({'NID': request.form['NID']})
    
    if login_user:
        if bcrypt.hashpw(request.form['NID'].encode('utf-8'), login_user['NID'].encode('utf-8')) == login_user['NID'].encode('utf-8'):
            session['NID'] = request.form['NID']
            return redirect(url_for('index'))
    return 'Invalid NID combination'

@app.route('/register', methods=['Get', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.student
        existing_user = users.find_one({'NID': request.form['NID']})

        if existing_user is None:
            # print(request.form['NID'])
            # print(request.form['Name'])
            # print(request.form['Dept'])
            # print(request.form['Average'])
            # print(request.form['Rank'])
            # print(request.form['Grade'])
            # print(request.form['Sex'])
            # print(request.form['Residence'])
            server.insert_student(request.form['NID'], request.form['Name'], request.form['Dept'], int(request.form['Grade']), float(request.form['Average']), int(request.form['Rank']), request.form['Sex'], request.form['Residence'])
            #session['NID'] = request.form['NID']
            return redirect(url_for('index'))

        return 'That NID already exists!'

    return render_template('register.html')


if __name__ == "__main__":
    app.run(host ='127.0.0.1')