from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open('index.html', 'r') as f:
        text = f.read()
    return text




@app.route('/login')
def login():
    with open('login.html', 'r') as f:
        text = f.read()
    return text


app.run()