from sqlalchemy import UniqueConstraint
from app import db

class Farmer(db.Model):
    __tablename__ = 'Farmer'
    farmerID = db.Column(db.Integer,  nullable=False, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    UniqueConstraint (farmerID)
    def __repr__(self):
        return " {} {}".format(self.farmerID, self.firstName)

class Food(db.Model):
    __tablename__ = 'Food'
    foodID = db.Column(db.Integer, nullable=False, primary_key=True, ) 
    foodType = db.Column(db.String(50), nullable=False, default='produce')
    foodName = db.Column(db.String(50), nullable=False) 
    UniqueConstraint (foodID, foodName)
    def __repr__(self):
        return " {} {}".format(self.foodID,  self.foodType) 

class Auction(db.Model):
    __tablename__= 'Auction'
    auctionID = db.Column(db.Integer, nullable=False, primary_key=True)
    auctionDate = db.Column(db.Date, nullable=False)
    auctionName = db.Column(db.String(100), nullable=False)
    auctionStreet = db.Column(db.String(50), default='NULL')
    auctionCity = db.Column(db.String(20), nullable=False)
    auctionState = db.Column(db.String(2), nullable=False, default='KY')
    auctionZip = db.Column(db.String(12), default='NULL')
    auctionCounty = db.Column(db.String(50), default='NULL')
    auctionPhone = db.Column(db.String(12), default='NULL')
    auctionContactName = db.Column(db.String(50), default='NULL')
    UniqueConstraint (auctionID)
    def __repr__(self):
        return " {} {}".format(self.auctionID,  self.auctionDate)

class FoodBank(db.Model):
    __tablename__='FoodBank'
    foodbankID = db.Column(db.Integer, nullable=False, primary_key=True)
    fbName = db.Column(db.String(45), nullable=False)
    fbStreet = db.Column(db.String(45), nullable=False)
    fbCity = db.Column(db.String(45), nullable=False)
    fbCounty = db.Column(db.String(45), nullable=False)
    fbState = db.Column(db.String(2), default='KY')
    fbZip = db.Column(db.String(12), nullable=False)
    fbPhoneNo = db.Column(db.String(12), nullable=False)
    contactName = db.Column(db.String(45), default='NULL')
    contactEmail = db.Column(db.String(100), default='NULL')
    contactPhoneNo = db.Column(db.String(12), default='NULL')
    UniqueConstraint (foodbankID, fbPhoneNo)
    def __repr__(self):
        return " {} {}".format(self.foodbankID,  self.fbName)

class Funder(db.Model):
     __tablename__='Funder'
     funderID = db.Column(db.Integer, nullable=False, primary_key=True)
     funderLink = db.Column(db.String(50), nullable=False)
     funderContactName = db.Column(db.String(50), nullable=False)
     funderContactEmail = db.Column(db.String(50), default='NULL')
     funderContactPhoneNo = db.Column(db.String(12), default='NULL')
     funderStreet = db.Column(db.String(50), default='NULL')
     funderCity = db.Column(db.String(50), default='NULL')
     funderState = db.Column(db.String(2), default='KY')
     funderZipcode = db.Column(db.String(12), nullable=False)
     UniqueConstraint (funderID)
     def __repr__(self):
        return " {} {}".format(self.funderID,  self.funderLink)

# resultFarmer = Farmer.query.all()
# resultFood = Food.query.all()
# resultAuction = Auction.query.all()
# resultFoodBank = FoodBank.query.all()
resultFunder = Funder.query.all()
#print (resultFarmer)
#print (resultFood)
#print (resultAuction)
#print (resultFoodBank)
print (resultFunder)
