from re import search
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from numpy import full
from sqlalchemy import create_engine, func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user1:feedingky#DBMS@127.0.0.1:3306/feedingky"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/search/<value>", methods=['GET'])
# Function call to render search results based on the option selected from the dropdown menu
def renderSearchPage(value):
    if value == "1":
        # total funding spent to show in summary
        from models import Invoices
        totalCost = Invoices.query.with_entities(
            func.sum(Invoices.totalCost)).all()
        # query all invoices to show in table
        invoices = Invoices.query.all()
        return render_template("search.html", value=totalCost, searchResults=invoices)
    elif value == "2":
        #  types of produce query
        from models import Food
        from models import PurchasedProduce
        # get distinct food with produce type
        produce = Food.query.with_entities(Food.foodID).filter(
            Food.foodType == "produce").distinct()
        producePurchased = PurchasedProduce.query.with_entities(PurchasedProduce.foodID, func.count(
            PurchasedProduce.foodID)).group_by(PurchasedProduce.foodID).filter(PurchasedProduce.foodID.in_(produce)).all()
        # Need to find the foodType in produce from the foodID in producePurchased
        # Using a join
        # result = PurchasedProduce.query.join(Food, full=True)
        # purchasedIDs=[]
        # for produce in producePurchased:
        #     purchasedIDs.append(producePurchased[0])
        # finalResults=[]

        return render_template("search.html", searchResults=producePurchased)
    elif value == "3":
        # pounds distributed
        from models import PurchasedProduce
        pounds = PurchasedProduce.query.with_entities(
            func.sum(PurchasedProduce.quantity)).all()
        purchasedQuantity = PurchasedProduce.query.all()
        return render_template("search.html", searchResults=purchasedQuantity, value=pounds)
    elif value == "4":
        # meals supplemented
        from models import Invoices
        pounds = Invoices.query.with_entities(
            func.sum(Invoices.totalPound)).all()
        mealSupplemented = pounds[0][0]/6
        invoices = Invoices.query.all()
        return render_template("search.html", value=mealSupplemented, searchResults=invoices)
    elif value == "5":
        # farmers that participate in program
        from models import Farmer
        counties = Farmer.query.with_entities(Farmer.county, func.count(
            Farmer.county)).group_by(Farmer.county).all()
        return render_template("search.html", searchResults=counties, value="")
    elif value == "6":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value == "7":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value == "8":
        # farmers that participate in program
        return render_template("selectError.html")
    elif value == "5":
        # farmers that participate in program
        return render_template("selectError.html")
    else:
        return render_template("selectError.html")
