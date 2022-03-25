from flask import (
    Flask,
    abort
)
from markupsafe import escape


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about')
def about():
    return '<h2>About Page!<h2>'

@app.route('/reverse/<name>')
def reverse_name(name):
    return f'<h1>{escape(name[::-1])}</h1>'


@app.route('/add/<int:no1>/<int:no2>')
def add_number(no1, no2):
    summ = no1 + no2
    return f'<h1>{escape(summ)}</h1>'


@app.route('/user/<int:id>')
def user_id(id):
    usr = ["Akshat", 'Ayan']
    try:
        return f'<h1>{usr[id]}</h1>'
    except IndexError:
        abort(404)

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))


if __name__ == "__main__":
    app.run(debug=True)