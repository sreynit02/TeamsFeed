from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sreynit:berea@127.0.0.1:3307/feedingky'
app.config['SQLALCHEMY_ECHO'] = True;
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template("index.html")
