from flask import Flask
app = Flask(__name__)


@app.route('/sample')
def hello_world():
<<<<<<< HEAD
    return '<h1>Hello Döni!!!</h1>'
||||||| merged common ancestors
    return '<h1>Hello, Flask!</h1>'
=======
    return '<h1>Hello, Class!</h1>'
>>>>>>> upstream/main


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
