from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import average, full
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

#create flask application and import database (be sure to put in your username/password/name of database)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:Superliminal2019!@127.0.0.1:3306/feedky"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

#default function that calls main page
@app.route("/")
def render_homepage():
    return render_template("index.html")

#run the route that is connected to the search page
@app.route("/search/<value>", methods=['GET', 'POST'])
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
        
        producePurchased = Food.query.join(PurchasedProduce, Food.foodID == PurchasedProduce.foodID).add_columns(Food.foodName, func.sum(PurchasedProduce.quantity * PurchasedProduce.unitPrice)).filter(Food.foodID == PurchasedProduce.foodID).group_by(Food.foodName).all()
        


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
        countyList = []
        for county in counties:
            tempList = []
            tempList.append(county[0])
            tempList.append(county[1])
            countyList.append(tempList)
        return render_template("search.html", searchResults=counties, countyList=countyList)
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
        # Farmers who received more than $10000
        farmerGrant = Invoices.query.with_entities(Invoices.farmerID).filter(Invoices.totalCost > 10000).distinct()
        farmerName = Farmer.query.with_entities(Farmer.firstName).filter(Farmer.farmerID.in_(farmerGrant)).all()
        print(list(farmerName))
        return render_template("search.html", searchResults = farmerName)
    else:
        return render_template("selectError.html")
