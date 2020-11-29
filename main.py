from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import server
import os
import time
import base64
import qrcode


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
        return render_template('home_page.html', nid = session.get('username'))
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
            server.insert_money2(nid,  data, 10, 1)
            return redirect(url_for('index'))
        return render_template('register_student.html')
    return render_template('register_student.html')

@app.route('/register/teacher', methods=['Get', 'POST'])
def register_teacher():
    if request.method == 'POST':
        nid = session.get('username')
        if nid is not None and 'T' in nid:
            server.insert_teacher(nid, request.form['Name'], request.form['Dept'])
            server.create_moneybag(nid) #create bag
            data = time.strftime("%Y-%m-%d",time.localtime()) #format time
            server.insert_money2(nid,  data, 1000, 1)
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
    nid = session.get('username')
    record = server.find_teactive(nid) #get self activity record from db
    if request.method == 'POST':
        server.insert_active(request.form['ActiveName'], nid, int(request.form['Credit']))
        return redirect(url_for('activity_teacher'))
    return render_template('activity_teacher.html', record = record)

@app.route('/activity_student', methods=['Get', 'POST'])
def activity_student():
    nid = session.get('username')
    record = server.find_active() #get activity record from db
    record2 = server.find_stchooseactive(nid) #get activity record from db
    if request.method == 'POST':
        server.choose_active(nid,request.get_json()['TNID'],request.get_json()['ActivityName'])
        return redirect(url_for('activity_student'))
    return render_template('activity_student.html', record = record, record2 = record2)

@app.route('/see_student', methods=['Get', 'POST'])
def see_student():
    nid = session.get('username')
    aid = request.cookies.get('AID')
    record = server.find_techooseactive(nid,aid)
    if request.method == 'POST':
        return render_template('see_student.html',record = record)
    return render_template('see_student.html',record = record)

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
        record = server.find_stmoneyhistory(nid)
        return render_template('moneybag_student.html', nid = nid, money = money ,record = record)
    return redirect(url_for('login'))

@app.route('/moneybag_teacher', methods=['Get','POST'])
def moneybag_teacher():
    nid = session.get('username')
    if nid is not None: 
        money = server.find_money(nid)
        record  = server.find_temoneyhistory(nid)
        return render_template('moneybag_teacher.html', nid = nid, money = money ,record = record)
    return redirect(url_for('login'))

def return_img_stream(img_local_path):
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
    return img_stream

qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_Q,box_size=10, border=1,)

@app.route('/qrcode')
def qrcode():
    sendNID = request.cookies.get('sendNID')
    reason = request.cookies.get('reason')
    aid = request.cookies.get('AID')
    tnid = session.get('username')
    url = 'http://127.0.0.1:5000/qrcode_getpoint'
    url += '?SNID='+sendNID+'&'+'TNID='+tnid+'&'+'AID='+aid+'&'+'reason='+str(reason)
    qr.add_data(url) 
    qr.make(fit=True)
    img = qr.make_image()
    img.save("QRcode.png") # 儲存圖片 1點
    img_path = 'D:/python/無現金校園系統/nocashschoolsys/QRcode.png' #qrcode於本機端的位置
    img_stream = return_img_stream(img_path)
    return render_template('index.html',img_stream=img_stream)

@app.route('/qrcode_getpoint', methods=['GET','POST'])
def qrcode_getpoint():
    snid = request.args.get('SNID', default=None, type=str)
    tnid = request.args.get('TNID', default=None, type=str)
    aid = request.args.get('AID', default=None, type=str)
    reason = request.args.get('reason', default=0, type=int)
    data = time.strftime("%Y-%m-%d",time.localtime()) #format time
    if reason == 2 or reason == 3: get = 1
    elif reason == 4: get = 2
    elif reason == 5: get = 5
    else: get = 3
    server.insert_money(tnid,snid,aid,data,get,reason)
    session['username'] = snid
    if request.method == 'POST':
            return redirect(url_for('moneybag_student'))
    return redirect(url_for('moneybag_student'))

if __name__ == "__main__":
    app.run(host ='127.0.0.1')