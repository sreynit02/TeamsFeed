from flask import Flask, render_template
# from exts import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user1:feedingky#DBMS@127.0.0.1:3306/feedingky'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# def register_extensions(app):
#     db.init_app(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
# Function call to render search page
def renderSearchPage():
    from models import Farmer
    farmers = Farmer.query.all()
    return render_template("search.html", farmers=farmers)
