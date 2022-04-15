from gettext import install
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search")
# Function call to render search page
def renderSearchPage():
    return render_template("search.html")
