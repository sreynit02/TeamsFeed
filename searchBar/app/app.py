from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:password@127.0.0.1:3306/feedingky"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search/<value>", methods=['GET'])
# Function call to render search results based on the option selected from the dropdown menu

def renderSearchPage(value):
    if value=="1":
        # funding spent query
        return render_template("selectError.html")
    elif value=="2":
        #  types of produce query
        return render_template("selectError.html")
    elif value=="3":
        # pounds distributed
        return render_template("selectError.html")
    elif value=="4":
        # meals supplemented
        return render_template("selectError.html")
    elif value=="5":
        # farmers that participate in program
        from models import Farmer
        counties = Farmer.query.with_entities(Farmer.county, func.count(
            Farmer.county)).group_by(Farmer.county).all()
        return render_template("search.html", searchResults=counties)
    elif value=="5":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value=="6":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value=="7":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value=="8":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value=="5":
        # farmers that participate in program
        return render_template("selectError.html")
    else:
        return render_template("selectError.html")

