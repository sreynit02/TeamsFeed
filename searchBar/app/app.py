from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:Superliminal2019!@127.0.0.1:3306/feedky'
app.config['SQLALCHEMY_ECHO'] = True;
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search")
# Function call to render search page
def renderSearchPage():
    return render_template("search.html")
