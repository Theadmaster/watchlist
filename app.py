from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
   return '<h1>Hello Gert!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user(name):
    return f'User: {escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user', name = 'gert'))
    print(url_for('user', name = 'allen'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test Page'