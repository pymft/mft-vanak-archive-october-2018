from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user/<name>&<int:n>')
def test(name, n):
    return render_template('user.html', name=name, n=n)


@app.route('/table/<int:m>&<int:n>')
def table(m, n):
    return render_template('table.html', m=m, n=n)


app.run(host='0.0.0.0', port='5000')
# app.run()