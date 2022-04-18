from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@127.0.0.1:3306/feedingky'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search")
# Function call to render search page
def renderSearchPage():
    return render_template("search.html")
