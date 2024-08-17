from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def foo():
    greeting = "Пиво это круто, но не для всех!Ы"
    return render_template("foo.html", greeting=greeting)

if __name__ == "__main__":
    app.run()