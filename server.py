from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/blog')
def blog():
    return 'This page is blog page'


@app.route('/blog/2024/dogs')
def blog_post():
    return 'This is my dog'
