from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import average, full
from sqlalchemy import create_engine, func

# create flask application and import database (be sure to put in your username/password/name of database)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://User1:Berea#CSC330@127.0.0.1:3306/feedingky"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# default function that calls main page


@app.route("/")
def render_homepage():
    return render_template("index.html")

# run the route that is connected to the search page


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
        tableHeader = ["Invoice Number", "Date Received",
                       "Date Paid", "Total Pounds", "Total Cost"]
        return render_template("search.html", tableHeader=tableHeader, option=value, value=totalCost, searchResults=invoices)
    elif value == "2":
        #  types of produce query
        from models import Food
        from models import PurchasedProduce
        # get distinct food with produce type
        produce = Food.query.with_entities(Food.foodID).filter(
            Food.foodType == "produce").distinct()
        producePurchased = PurchasedProduce.query.with_entities(PurchasedProduce.foodID, func.count(
            PurchasedProduce.foodID)).group_by(PurchasedProduce.foodID).filter(PurchasedProduce.foodID.in_(produce)).all()
        tableHeader = ["Food name", "Quantity of produce"]
        return render_template("search.html", searchResults=producePurchased, tableHeader=tableHeader)
    elif value == "3":
        # pounds distributed; display a table with invoiceNo, totalPounds,Farmer FirstName, Farmer LastName, and grant used to pay
        from models import PurchasedProduce
        pounds = PurchasedProduce.query.with_entities(
            func.sum(PurchasedProduce.quantity)).all()
        purchasedQuantity = PurchasedProduce.query.all()
        tableHeader = ["Invoice Number", "Total pounds purchased",
                       "Farmer First Name", "Farmer Last Name", "Grant used to pay"]
        return render_template("search.html", searchResults=purchasedQuantity, value=pounds, tableHeader=tableHeader)
    elif value == "4":
        # meals supplemented = total Pounds/0.06
        from models import Invoices
        pounds = Invoices.query.with_entities(
            func.sum(Invoices.totalPound)).all()
        mealSupplemented = pounds[0][0]/6
        invoices = Invoices.query.all()
        # Pie chart displays the total meals supplied by each grant
        GrantTotal = Invoices.query.with_entities(Invoices.grantID, func.sum(
            Invoices.totalCost)/0.06).group_by(Invoices.grantID).all()
        # TO DO: Get grant Name from grantID so as to display grant names instead of ID

        GrantTotalList = []
        for total in GrantTotal:
            tempList = []
            tempList.append(str(total[0]))
            tempList.append(total[1])
            GrantTotalList.append(tempList)
        tableHeader = ["Invoice Number", "Date Received",
                       "Date Paid", "Total Pounds", "Total Cost"]
        title="Number of meals supplemented by grants"
        return render_template("search.html",chartTitle=title, option=value, tableHeader=tableHeader, value=mealSupplemented, searchResults=GrantTotal, chartList=GrantTotalList)
    elif value == "5":
        # farmers that participate in program
        from models import Farmer
        farmers = Farmer.query.all()
        cities = Farmer.query.with_entities(Farmer.city, func.count(
            Farmer.city)).group_by(Farmer.city).all()
        cityList = []
        for county in cities:
            tempList = []
            tempList.append(county[0])
            tempList.append(county[1])
            cityList.append(tempList)
        tableHeader = ["County", "Number of Farmers"]
        title="Number of farmers per city"
        tableHeader = ["First Name", "Last Name",
                       "Phone Number", "City", "County", "State"]
        return render_template("search.html", chartTitle=title,tableHeader=tableHeader, option=value, searchResults=farmers,chartList=cityList)
    elif value == "6":
        # which Kentucky counties are the farmers from
        # TO DO: Order these by county
        from models import Farmer
        counties = Farmer.query.with_entities(Farmer.county, func.count(
            Farmer.county)).group_by(Farmer.county).all()
        countyList = []
        for county in counties:
            tempList = []
            tempList.append(county[0])
            tempList.append(county[1])
            countyList.append(tempList)
        tableHeader = ["County", "Number of Farmers"]
        title="Number of farmers per county"
        return render_template("search.html", chartTitle=title,tableHeader=tableHeader, option=value, searchResults=counties, chartList=countyList)
    elif value == "7":
        # Average amount paid to farmers
        # TO DO: Add a join with Farmer table so as to display the farmer name instead of IDs
        from models import Invoices
        average = Invoices.query.with_entities(
            func.avg(Invoices.totalCost)).all()
        invoices = Invoices.query.all()
        tableHeader = ["Farmer's first name",
                       "Farmer's Last Name", "Amount paid"]
        return render_template("search.html", option=value, value=average, searchResults=invoices, tableHeader=tableHeader)
        # tableHeader = ["Invoice Number", "Date Received",
        #                "Date Paid", "Total Pounds", "Total Cost"]
        # return render_template("search.html", tableHeader=tableHeader, option = value, value=average, searchResults=invoices)
    elif value == "8":
        from models import Invoices
        from models import Farmer
        # Farmers who received more than $10000
        # TO DO: Check this query. It does not return any thing
        farmerGrant = Invoices.query.with_entities(
            Invoices.farmerID).filter(Invoices.totalCost > 10000).distinct()
        farmerName = Farmer.query.with_entities(Farmer.firstName).filter(
            Farmer.farmerID == farmerGrant).distinct()
        tableHeader = ["Farmer's first name",
                       "Farmer's Last Name", "Amount paid"]
        return render_template("search.html", option=value, farmerName=farmerGrant, tableHeader=tableHeader)
    else:
        return render_template("selectError.html")
