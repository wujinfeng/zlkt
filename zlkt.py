from flask import Flask, url_for, request, make_response, render_template, redirect, abort
from werkzeug.utils import secure_filename
from models import User
from exts import db

import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/me', methods=['GET', 'POST'])
def me():
    if request.method == 'POST':
        return 'post'
    return 'my name wu'


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/child')
def child():
    return render_template('child.html')


@app.route('/user/<username>')
def show_user_profile(username=None):
    return 'user: %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/pro/')
def projects():
    app.logger.debug('debug...')
    app.logger.warning('A warning (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'the pro'


@app.route('/about')
def about():
    return redirect(url_for('login'))


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'u' and password == 'p':
            error = ''
        else:
            error = 'Invalid username/password'
        return render_template('login.html', error=error)
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        telephone = request.form['telephone']
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        # 手机号码验证，如果被注册了，不能再注册
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该手机号已经被注册，请更换手机号！'
        else:
            # password1 password2判断相等
            if password2 != password1:
                return '两次密码不一样，请核对后再填写！'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                # 注册ok，跳转登陆页面
                return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('regist.html')


@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html'), 500)
    resp.headers['X-Something'] = 'A value'
    return resp


if __name__ == '__main__':
    app.run(port=3000)

#     username = request.cookies.get('username')
#     print(username)
#     print(url_for('me'))
#     print(url_for('show_user_profile', username='wu'))
#     resp = make_response(render_template('hello.html', name='index'))
#     resp.set_cookie('username', 'the username')
#     return resp
