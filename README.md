# TeamsFeed

## Contributors:  

### Team members:  

1. Concepta Njolima  
2. Sreynit Khatt  
3. Tawanda Kumbula  
4. Luke Wilson  

### Professors and TAs:

1. Dr. Jasmine Jones  
2. Professor Deanna Wilborne  
3. Ahmed Abdulahi  
4. Emiliano Torres-Vera  
5. Immanuela Belaineh  

## Problem statement:  
For over 50 years, FeedingKY has not collected enough detailed information from farmers, especially about their main crops. Feeding KY needs to reformat its existing database to track farmers' information to track where grant money is being spent.


## Goal
Our goal is to create a database that can effectively use queries to give the user data about farmers, crops, and where grant money goes.


## Business Rule 
1. A farm can only be assigned to one county. 
2. The quantity of the food is from the farmers invoice dropped by the farmer at the foodbank. The invoice is then sent to FeedingKY from the foodbank. The invoice is used to keep track of where produce goes and the price of that produce. This helps keep track of grant money spent.  
3. A farmer must own at least one farm with an address because FeedingKY mostly works with farmers in the state.  
4. A farmer must be a resident of Kentucky
5. A farmer can grow one or many crops
6. A farmer can donate any crop (accept other crops except berries and honey)
7. A farmer can have more than one invoice
8. Each farmer is assigned an ID number 
9. Farmer’s first/last name is recorded, their county, and address
10. Each invoice is assigned an ID
11. A farmer can sell their produce to FeedingKY at an auction or a food bank
12. There is only one food bank per county, but not all counties in KY have a food bank. Each food bank needs an address because feedingKY only donates to food banks in KY.  
13. Food has name and type.

## ER diagram
The Entity-relationship diagram is as shown below:

<image src="https://github.com/sreynit02/TeamsFeed/blob/main/Copy%20of%20PM01_%20Problem%20Statement%20and%20E-R%20Diagram.drawio.png">
