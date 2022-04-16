from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@host/database'
app.config['SQLALCHEMY_ECHO'] = True;
db = SQLAlchemy(app)

from models import Farmer
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search", methods = ['GET'])
# Function call to render search page
def renderSearchPage():
    farmers = Farmer.query.all()
    return render_template("search.html", farmers=farmers)
