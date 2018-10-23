from flask import Flask
from flask import request
from flask import render_template

webapp = Flask(__name__)

@webapp.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')        # 返回首页

@webapp.route('/signin', methods = ['GET'])
def signin_form():
    return render_template('form.html')          # 返回表单的页面

@webapp.route('/signin', methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin_ok.html', username=username)              # 返回登录成功的页面，并传入username数据
    return render_template('form.html', message='Bad username or password', username=username)

if __name__=='__main__':
    webapp.run()
