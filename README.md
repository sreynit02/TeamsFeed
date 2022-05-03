# TeamsFeed

## Contributors:  

### Team members:  

1. Concepta Njolima  
2. Sreynit Khatt  
3. Tawanda Kumbula  
4. Luke Wilson  

### Community Partner
1. Sarah Vaughn from Feeding Kentucky 

### Professors and TAs:

1. Dr. Jasmine Jones  
2. Professor Deanna Wilborne  
3. Ahmed Abdulahi  
4. Emiliano Torres-Vera  
5. Immanuela Belaineh  

## Problem statement:  
For over 10 years, FeedingKY has not collected enough detailed information from farmers, especially about their main crops. Feeding KY needs to reformat its existing database to track farmers' information to track where grant money is being spent.


## Goal
Our goal is to create a database that can effectively use queries to give the user data about farmers, crops, and where grant money goes.


## Project description
This project contains three parts: project management, data modeling, and application development. 

The data modeling part started with client meetings to better understand the business rules of Feeding Kentucky which helped us develop an Entity-Relationship(ER) Diagram. Then we normalized the data model we had developed to ensure it represented the business rules from our community partner and did not contain anomalies.

The project management part of the project involved brainstorming viable solutions to the problem statement identified. We shared our solution ideas with the client before deciding to develop a search application. With the confirmation from our client and the knowledge of the available resources, we started prototyping the solution. The prototyping phase included sketching, and developing user flows and wireframes for our solution.

Then, we proceeded to the project development phase. The search feature contains a search bar and a results page. The search bar is the area where a user selects what they want to search for in the database. The search bar contains a dropdown menu of questions that Sarah Vaughn frequently wants to answer using the information. After the user selects a question, the application runs a SQL query that fetches the answer and displays the results on a new page. We represent our results in tabular and graphical forms. We used Bootstrap data tables for the tabular representation of the results. Using data tables allowed us to add searching, sorting, pagination, and export features to the tables. The Export functionality enables a user to copy or download an Excel or PDF version of the table. This is specifically useful when a user wants to perform advanced computations with the data in Excel or attach the results to a report in pdf form The visualizations are pie charts or bar graphs. The visualization is implemented by using Google Chart API which displays the result of a query in pie and bar charts. 

Some of the software requirements are WLS2 for Windows/ Ubuntu or Linux or MacOS terminal, Docker, Virtual Environment, Python3, and MySQL Workbench. To develop our application, we used the Flask web framework, MySQL, Python, HTML, Javascript, and Flask-SQLAlchemy. 

## Business Rule 
1. A farm can only be assigned to one county. 
2. The quantity of the food is from the farmers invoice dropped by the farmer at the foodbank. The invoice is then sent to FeedingKY from the foodbank. The invoice is used to keep track of where produce goes and the price of that produce. This helps keep track of grant money spent.  
3. A farmer must own at least one farm with an address because FeedingKY mostly works with farmers in the state.  
4. A farmer must be a resident of Kentucky
5. A farmer can grow one or many crops
6. A farmer can donate any crop (except berries and honey)
7. A farmer can have more than one invoice
8. Each farmer is assigned an ID number 
9. Farmer’s first/last name is recorded, their county, and address
10. Each invoice is assigned an ID
11. A farmer can sell their produce to FeedingKY at an auction or a food bank
12. There is only one food bank per county, but not all counties in KY have a food bank. Each food bank needs an address because feedingKY only donates to food banks in KY.  
13. Food has name and type.
14. Food that is donated will be put on an invoice and the price will be $0.
15. Each grant has at least 1 funder.

## Summary of Changes:  
Our business rules and problem statement from milestone 1 to milestone 3. At first, our problem statement focused on farmer information but after speaking 
to the client, we realized that our problem statement should focus on annual financial reports. Also, after speaking to the client, we found out that
we were not restricted to just 28 crops (only honey, berries, and some meats). We also found out that KY Kids Eat did not exist anymore. These two business
rules were changed and adjusted with minor tweaks to our business rules.

## ER diagram
The Entity-relationship diagram is as shown below:

<image src="https://github.com/sreynit02/TeamsFeed/blob/main/Updated_ERD_FeedingKY.png">
  
## User Journey
  
##   
