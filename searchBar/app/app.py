from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func


engine = create_engine(
    "mysql+pymysql://user1:feedingky#DBMS@127.0.0.1:3306/feedingky",
)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@127.0.0.1:3306/feedingky'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search", methods=['GET'])
# Function call to render search page
def renderSearchPage():
    from models import Farmer
    # farmers = Farmer.query.all()
    counties = Farmer.query.with_entities(Farmer.county, func.count(
        Farmer.county)).group_by(Farmer.county).all()
    # query = db.select(Farmer.county).count()
    # result = engine.execute(query).fetchall()
    return render_template("search.html", counties=counties)
