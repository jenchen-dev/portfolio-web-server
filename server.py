from flask import Flask, render_template
app = Flask(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)


@app.route('/blog')
def blog():
    return 'This page is blog page'


@app.route('/blog/2024/dogs')
def blog_post():
    return 'This is my dog'
