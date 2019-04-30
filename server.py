from flask import Flask, render_template
app = Flask(__name__)


# @app.route("/<name>")
# def index(name):
#     name = name.upper()
#     return render_template('index.html', name=name)


@app.route("/")
def index1():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)


@app.route("/another")
def show():
    return '<h1>Yo</h1>'


@app.route('/user/<username>')
def username(username):
    return f'Hi {username}'


if __name__ == '__main__':
    app.run()
