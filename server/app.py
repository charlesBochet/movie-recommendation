from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/my-movies')
def list_user_movies():
    return render_template('my-movies.html', page_title='My Movies')
