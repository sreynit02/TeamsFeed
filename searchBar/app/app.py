from re import search
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from numpy import average, full
from sqlalchemy import create_engine, func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sreynit:berea@127.0.0.1:3307/feedingky"
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
        farmers = Farmer.query.all()
        return render_template("search.html", searchResults=farmers)
    elif value == "6":
        # which Kentucky counties are the farmers from
        from models import Farmer
        counties = Farmer.query.with_entities(Farmer.county, func.count(
            Farmer.county)).group_by(Farmer.county).all()
        return render_template("search.html", searchResults=counties)
    elif value == "7":
        # Average amount paid to farmers
        from models import Invoices
        average = Invoices.query.with_entities(
            func.avg(Invoices.totalCost)).all()
        invoices = Invoices.query.all()
        return render_template("search.html", value=average, searchResults=invoices)
    elif value == "8":
        from models import Invoices
        from models import Farmer
        # Farmers who received more than $1000
        farmerGrant = Invoices.query.with_entities(Invoices.farmerID).filter(Invoices.totalCost > 1000).distinct()
        farmerName = Farmer.query.with_entities(Farmer.firstName).filter(Farmer.farmerID == farmerGrant).distinct()
        return render_template("search.html", farmerName = farmerName)
    else:
        return render_template("selectError.html")
