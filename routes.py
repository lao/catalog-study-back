from . import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/catalog')
def catalog():
    return "I am your catalog!"