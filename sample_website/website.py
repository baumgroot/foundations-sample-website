from flask import Flask
app = Flask(__name__)


@app.route('/sample')
def hello_world():
    return '<h1>Hello Döni!!!</h1>'


@app.route('/index')
def index(name=None):
    file = open("./sample_website/index.html", "r")
    text = file.read()
    print(text)
    return text


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
