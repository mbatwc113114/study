from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
        return "aman"

app.run('0.0.0.0')
