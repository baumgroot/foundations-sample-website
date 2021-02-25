from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/sample')
def hello_world():
    return '<h1>Hello Döni!!!</h1>'


@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
