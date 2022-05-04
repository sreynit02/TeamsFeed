from decimal import ROUND_UP
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import average, full
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# create flask application and import database (be sure to put in your username/password/name of database)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user1:feedingky#DBMS@127.0.0.1:3306/feedingky"

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
        from models import Grant
        totalCost = Invoices.query.with_entities(
            func.sum(Invoices.totalCost)).all()[0][0]
        totalCost = round(totalCost, 2)
        # query all invoices to show in table
        invoices = Invoices.query.all()

        # TO DO: Pie chart to display the total funding from each grant: Join the invoices and grant tables
        # TO DO: Should this total spending be restricted to the annual year?
        FundingCosts = Invoices.query.join(Grant, Invoices.grantID==Grant.grantID).add_columns(Grant.grantName, func.sum(Invoices.totalCost)).group_by(Invoices.grantID).all()
        print(FundingCosts)
        fundingList = []
        for funding in FundingCosts:
            tempList = []
            tempList.append(str(funding[1]))
            tempList.append(funding[2])
            fundingList.append(tempList)
        title="Total funding per grant"
        summaryTitle="The total funding spent"
        tableTitle="Invoice details"
        tableHeader = ["Invoice Number", "Date Received",
                       "Date Paid", "Total Pounds", "Total Cost","Grant used"]

        return render_template("search.html", tableTitle=tableTitle, tableHeader=tableHeader,chartTitle=title, option=value, summaryValue=totalCost, summaryTitle=summaryTitle, chartList=fundingList,searchResults=invoices)

    elif value == "2":
        #  types of produce query
        from models import Food
        from models import PurchasedProduce
        # get distinct food with produce type
        producePurchased = Food.query.join(PurchasedProduce, Food.foodID == PurchasedProduce.foodID).add_columns(Food.foodName, func.round(func.sum(PurchasedProduce.quantity * PurchasedProduce.unitPrice))).filter(Food.foodID == PurchasedProduce.foodID).group_by(Food.foodName).all()
        title="Amount of produce purchased per food type"
        tableTitle="Details of purchased produce"
        tableHeader = ["Food name", "Quantity of produce"]
        foodCostList = []
        for produce in producePurchased:
            tempList = []
            tempList.append(str(produce[1]))
            tempList.append(int(produce[2]))
            foodCostList.append(tempList)
        return render_template("searchColumn.html", tableTitle=tableTitle, option=value, chartTitle=title,searchResults=producePurchased, tableHeader=tableHeader, chartList=foodCostList)

    elif value == "3":
        # pounds distributed
        from models import PurchasedProduce
        from models import Food
        pounds = PurchasedProduce.query.with_entities(
            func.sum(PurchasedProduce.quantity)).all()[0][0]
        food = Food.query.join(PurchasedProduce, Food.foodID == PurchasedProduce.foodID).add_columns(Food.foodName, func.round(func.sum(PurchasedProduce.quantity),2)).filter(Food.foodID == PurchasedProduce.foodID).group_by(Food.foodName).all()
        #foodQuantities=PurchasedProduce.query.with_entities(PurchasedProduce.foodID, func.sum(PurchasedProduce.quantity)).group_by(PurchasedProduce.foodID).all()
        foodQuntityList = []
        for quantity in food:
            tempList = []
            tempList.append(str(quantity[1]))
            tempList.append(int(quantity[2]))
            foodQuntityList.append(tempList)
        title="Total quantity of produce in pounds purchased for each food type "
        summaryTitle="Total pounds purchased"
        tableTitle="Details of pounds of food purchased"
        tableHeader = ["Food Name", "Total produce purchased","units"]
        return render_template("search.html", option=value, tableTitle=tableTitle, chartTitle=title,chartList=foodQuntityList,searchResults=food, summaryValue=pounds,summaryTitle=summaryTitle, tableHeader=tableHeader)

    elif value == "4":
        # meals supplemented = total Pounds/0.06
        from models import Invoices
        from models import Grant
        pounds = Invoices.query.with_entities(
            func.sum(Invoices.totalPound)).all()
        mealSupplemented = pounds[0][0]/6

        #Rounds off the meals supplemented to an integer
        mealSupplemented = round(mealSupplemented)

        invoices = Invoices.query.join(Grant, Invoices.grantID==Grant.grantID).add_columns(Invoices.invoiceNo, Invoices.dateReceived, Invoices.datePaid, Invoices.totalPound, Invoices.totalCost, Grant.grantName).all()
        # Pie chart displays the total meals supplied by each grant
        GrantTotal = Invoices.query.join(Grant, Invoices.grantID==Grant.grantID).add_columns(Grant.grantName, func.round((func.sum(Invoices.totalPound)/0.06),2)).group_by(Grant.grantName).all()
        GrantTotalList = []
        for total in GrantTotal:
            tempList = []
            tempList.append(str(total[1]))
            tempList.append(total[2])
            GrantTotalList.append(tempList)
        tableHeader = ["Invoice Number", "Date Received",
                       "Date Paid", "Total Pounds", "Total Cost","Grant"]
        title="Number of meals supplemented by different grants"
        tableTitle="Details of invoices"
        summaryTitle="Total Meals supplemented"
        return render_template("searchColumn.html", tableTitle=tableTitle, chartTitle=title, option=value, tableHeader=tableHeader, summaryValue=str(mealSupplemented),summaryTitle=summaryTitle, searchResults=invoices, chartList=GrantTotalList)
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
        tableTitle="List of farmers that participate in the program"
        tableHeader = ["First Name", "Last Name",
                       "Phone Number", "City", "County", "State"]
        return render_template("search.html", tableTitle=tableTitle, chartTitle=title,tableHeader=tableHeader, option=value, searchResults=farmers,chartList=cityList)
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
        tableTitle="Number of farmers per county"
        title="Number of farmers per county"
        return render_template("search.html", tableTitle=tableTitle, chartTitle=title,tableHeader=tableHeader, option=value, searchResults=counties, chartList=countyList)
        # Average amount paid to farmers
    elif value == "7":
        from models import Invoices
        from models import Farmer
        average = Invoices.query.with_entities(func.avg(Invoices.totalCost)).all()[0][0]

        #Round the average amount paid to farmers to 2 decimal
        average = round(average, 2)
        FarmerPayment=Invoices.query.join(Farmer,Invoices.farmerID==Farmer.farmerID).add_columns(Farmer.firstName,Farmer.lastName,func.round(func.avg(Invoices.totalCost),2)).filter(Invoices.farmerID==Farmer.farmerID).group_by(Invoices.farmerID).all()

        paymentList = []
        for payment in FarmerPayment:
            tempList = []
            tempList.append(str(payment[1]+" "+payment[2]))
            tempList.append(payment[3])
            paymentList.append(tempList)
        print(paymentList)
        title="Amount paid to every farmer"
        summaryTitle="Average amount paid to farmers"
        tableTitle="Details of amount paid to farmers "
        tableHeader = ["Farmer's first name",
                       "Farmer's Last Name", "Amount paid"]
        return render_template("searchColumn.html", tableTitle=tableTitle, chartTitle=title,option=value, chartList=paymentList,summaryValue=average,summaryTitle=summaryTitle, searchResults=FarmerPayment, tableHeader=tableHeader)

    elif value == "8":
        from models import Invoices
        from models import Farmer

        farmerName = Invoices.query.join(Farmer, Farmer.farmerID == Invoices.farmerID).add_columns(Farmer.firstName, Farmer.lastName, Invoices.totalCost).filter(Invoices.totalCost>10000).all()
        print(farmerName)
        farmerNameList = []
        for name in farmerName:
            tempList = []
            tempList.append(str(name[1] +" "+name[2]))
            tempList.append(name[3])
            farmerNameList.append(tempList)

        # TO DO: This would be better represented by a bar graph
        title="Farmers paid more than $10,000"
        tableTitle="List of farmers who earn more than $10,000"
        tableHeader = ["Farmer's first name",
                       "Farmer's Last Name", "Amount paid"]
        return render_template("searchColumn.html", searchResults = farmerName, tableTitle=tableTitle, chartList = farmerNameList, chartTitle=title,option=value, farmerName=farmerName, tableHeader=tableHeader)

    else:
        return render_template("selectError.html")
