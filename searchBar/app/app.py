from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import average, full
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# create flask application and import database (be sure to put in your username/password/name of database)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user:password@127.0.0.1:3306/feedingky"

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
            func.sum(Invoices.totalCost)).all()[0][0]
        # query all invoices to show in table
        invoices = Invoices.query.all()

        # TO DO: Pie chart to display the total funding from each grant: Join the invoices and grant tables
        # TO DO: Should this total spending be restricted to the annual year?
        FundingCosts = Invoices.query.with_entities(Invoices.grantID, func.sum(Invoices.totalCost)).group_by(Invoices.grantID).all()
        fundingList = []
        for funding in FundingCosts:
            tempList = []
            tempList.append(str(funding[0]))
            tempList.append(funding[1])
            fundingList.append(tempList)
        title="Total funding per grant"
        summaryTitle="The total funding spent"
        tableHeader = ["Invoice Number", "Date Received",
                       "Date Paid", "Total Pounds", "Total Cost","Grant used"]

        return render_template("search.html", tableHeader=tableHeader,chartTitle=title, option=value, summaryValue=totalCost, summaryTitle=summaryTitle, chartList=fundingList,searchResults=invoices)

    elif value == "2":
        #  types of produce query
        from models import Food
        from models import PurchasedProduce
        # get distinct food with produce type
        producePurchased = Food.query.join(PurchasedProduce, Food.foodID == PurchasedProduce.foodID).add_columns(Food.foodName, func.sum(PurchasedProduce.quantity * PurchasedProduce.unitPrice)).filter(Food.foodID == PurchasedProduce.foodID).group_by(Food.foodName).all()
        
        title="Amount of produce purchased per food type"
        tableHeader = ["Food name", "Quantity of produce"]
        return render_template("search.html", chartTitle=title,searchResults=producePurchased, tableHeader=tableHeader)
    elif value == "3":
        # pounds distributed
        from models import PurchasedProduce
        pounds = PurchasedProduce.query.with_entities(
            func.sum(PurchasedProduce.quantity)).all()
        # Table displays the food name, produce purchased and units
        # TO DO: Get food name after joining with food table
        purchasedQuantity = PurchasedProduce.query.all()
        # Pie chart displays the total quantity per foodID
        foodQuantities=PurchasedProduce.query.with_entities(PurchasedProduce.foodID, func.sum(PurchasedProduce.quantity)).group_by(PurchasedProduce.foodID).all()
        foodQuntityList = []
        for quantity in foodQuantities:
            tempList = []
            tempList.append(str(quantity[0]))
            tempList.append(int(quantity[1]))
            foodQuntityList.append(tempList)
        title="Total quantity of produce in pounds purchased for each food type "
        summaryTitle="Total pounds purchased"
        tableHeader = ["Food Name", "Total produce purchased","units"]
        return render_template("search.html", option=value, chartTitle=title,chartList=foodQuntityList,searchResults=purchasedQuantity, summaryValue=pounds,summaryTitle=summaryTitle, tableHeader=tableHeader)
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
                       "Date Paid", "Total Pounds", "Total Cost","Grant"]
        title="Number of meals supplemented by different grants"
        summaryTitle="Total Meals supplemented"
        return render_template("search.html",chartTitle=title, option=value, tableHeader=tableHeader, summaryValue=str(mealSupplemented),summaryTitle=summaryTitle, searchResults=invoices, chartList=GrantTotalList)
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
        #  Might be better displayed with some other graph
        from models import Invoices
        average = Invoices.query.with_entities(
            func.avg(Invoices.totalCost)).all()[0][0]
        invoices = Invoices.query.all()
        FarmerPayment=Invoices.query.with_entities(Invoices.farmerID, func.sum(Invoices.totalCost)).group_by(Invoices.farmerID).all()
        paymentList = []
        for payment in FarmerPayment:
            tempList = []
            tempList.append(str(payment[0]))
            tempList.append(payment[1])
            paymentList.append(tempList)
        title="Amount paid to every farmer"
        summaryTitle="Average amount paid to farmers"
        tableHeader = ["Invoice Number","Date received","Date Paid",
                       "Total Pounds", "Total Cost","Grant used"]
        return render_template("search.html", chartTitle=title,option=value, chartList=paymentList,summaryValue=average,summaryTitle=summaryTitle, searchResults=invoices, tableHeader=tableHeader)
        # tableHeader = ["Invoice Number", "Date Received",
        #                "Date Paid", "Total Pounds", "Total Cost"]
        # return render_template("search.html", tableHeader=tableHeader, option = value, value=average, searchResults=invoices)
    elif value == "8":
        from models import Invoices
        from models import Farmer
        # Farmers who received more than $10000
        farmerGrant = Invoices.query.with_entities(
            Invoices.farmerID).filter(Invoices.totalCost > 10000).distinct()
        farmerName = Farmer.query.with_entities(Farmer.firstName).filter(
            Farmer.farmerID == farmerGrant).distinct()
        # TO DO: This would be better represented by a bar graph
        title="Farmers paid more than $10,000"
        tableHeader = ["Farmer's first name",
                       "Farmer's Last Name", "Amount paid"]
        return render_template("search.html", chartTitle=title,option=value, farmerName=farmerGrant, tableHeader=tableHeader)
    else:
        return render_template("selectError.html")
