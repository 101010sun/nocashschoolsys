# render_template :樣式模板使用 HTML 撰寫，後台處理使用 Python
# server.py       :連接資料庫
# request         :request請求來與HTML互動
from  flask import Flask, render_template, request
import server


app = Flask(__name__)
# open debugger
app.config['DEBUG'] = True

#find the person by NID
@app.route('/user/<string:NID>')

#homepage
@app.route('/', methods=['GET'])
def main():
     name = request.args.get('name')
     return 'My name is {}'.format('10sun')

@app.route('/login', methods=['POST'])
def result():
    if request.method == 'POST':
        nid = request.values['NID']
        return render_template('home_page.html', name=nid)

if __name__ == "__main__":
    app.run(host ='127.0.0.1')