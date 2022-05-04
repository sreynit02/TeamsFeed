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
Our goal is to create an application that allows Sarah to easily view results for frequently asked questions about farmers and how grant funds are spent.


## Project description
This project contains three parts: project management, data modeling, and application development. 

The data modeling part started with client meetings to better understand the business rules of Feeding Kentucky which helped us develop an Entity-Relationship(ER) Diagram. Then we normalized the data model we had developed to ensure it represented the business rules from our community partner and did not contain anomalies.

The project management part of the project involved brainstorming viable solutions to the problem statement identified. We shared our solution ideas with the client before deciding to develop a search application. With the confirmation from our client and the knowledge of the available resources, we started prototyping the solution. The prototyping phase included sketching, and developing user flows and wireframes for our solution.

Then, we proceeded to the project development phase. The search feature contains a search bar and a results page. The search bar is the area where a user selects what they want to search for in the database. The search bar contains a dropdown menu of questions that Sarah Vaughn frequently wants to answer using the information. After the user selects a question, the application runs a SQL query that fetches the answer and displays the results on a new page. We represent our results in tabular and graphical forms. We used Bootstrap data tables for the tabular representation of the results. Using data tables allowed us to add searching, sorting, pagination, and export features to the tables. The Export functionality enables a user to copy or download an Excel or PDF version of the table. This is specifically useful when a user wants to perform advanced computations with the data in Excel or attach the results to a report in pdf form The visualizations are pie charts or bar graphs. The visualization is implemented by using Google Chart API which displays the result of a query in pie and bar charts. 

Some of the software requirements are WLS2 for Windows/ Ubuntu or Linux or MacOS terminal, Docker, Virtual Environment, Python3, and MySQL Workbench. To develop our application, we used the Flask web framework, MySQL, Python, HTML, Javascript, and Flask-SQLAlchemy. 


## ER diagram
The Entity-relationship diagram is as shown below:

<image src="https://github.com/sreynit02/TeamsFeed/blob/main/Updated_ERD_FeedingKY.png">
  
## Feeding Kentucky Application Preview
<!--   [![Watch the video](https://img.youtube.com/vi/5l12pmdiiEY/0.jpg)](https://youtu.be/5l12pmdiiEY) -->
  https://user-images.githubusercontent.com/54441700/166608366-aaeeb466-22d3-4c19-b7ee-4b17d08ca3ff.mp4
