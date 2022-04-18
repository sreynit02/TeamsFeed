from email.policy import default
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import TINYINT
from app import db


class Farmer(db.Model):
    __tablename__ = 'Farmer'
    farmerID = db.Column(db.Integer,  nullable=False, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    UniqueConstraint(farmerID)
<<<<<<< HEAD
=======
    foreignKeyFarmer = db.relationship('Invoices', back_populates='farmer_ID')
>>>>>>> modelContinued

    def __repr__(self):
        return " {} {}".format(self.farmerID, self.firstName)


class Food(db.Model):
    __tablename__ = 'Food'
    foodID = db.Column(db.Integer, nullable=False, primary_key=True, )
    foodType = db.Column(db.String(50), nullable=False, default='produce')
    foodName = db.Column(db.String(50), nullable=False)
<<<<<<< HEAD
    UniqueConstraint(foodID, foodName)

    def __repr__(self):
        return " {} {}".format(self.foodID,  self.foodType)


# class Auction(db.Model):
#     __tablename__ = 'Auction'
#     auctionID = db.Column(db.Integer, nullable=False, primary_key=True)
#     auctionDate = db.Column(db.Date, nullable=False)
#     auctionName = db.Column(db.String(100), nullable=False)
#     auctionStreet = db.Column(db.String(50), default='NULL')
#     auctionCity = db.Column(db.String(20), nullable=False)
#     auctionState = db.Column(db.String(2), nullable=False, default='KY')
#     auctionZip = db.Column(db.String(12), default='NULL')
#     auctionCounty = db.Column(db.String(50), default='NULL')
#     auctionPhone = db.Column(db.String(12), default='NULL')
#     auctionContactName = db.Column(db.String(50), default='NULL')
#     UniqueConstraint(auctionID)

#     def __repr__(self):
#         return " {} {}".format(self.auctionID,  self.auctionDate)


# class FoodBank(db.Model):
#     __tablename__ = 'FoodBank'
#     foodbankID = db.Column(db.Integer, nullable=False, primary_key=True)
#     fbName = db.Column(db.String(45), nullable=False)
#     fbStreet = db.Column(db.String(45), nullable=False)
#     fbCity = db.Column(db.String(45), nullable=False)
#     fbCounty = db.Column(db.String(45), nullable=False)
#     fbState = db.Column(db.String(2), default='KY')
#     fbZip = db.Column(db.String(12), nullable=False)
#     fbPhoneNo = db.Column(db.String(12), nullable=False)
#     contactName = db.Column(db.String(45), default='NULL')
#     contactEmail = db.Column(db.String(100), default='NULL')
#     contactPhoneNo = db.Column(db.String(12), default='NULL')
#     UniqueConstraint(foodbankID, fbPhoneNo)

#     def __repr__(self):
#         return " {} {}".format(self.foodbankID,  self.fbName)


# class Funder(db.Model):
#     __tablename__ = 'Funder'
#     funderID = db.Column(db.Integer, nullable=False, primary_key=True)
#     funderLink = db.Column(db.String(50), nullable=False)
#     funderContactName = db.Column(db.String(50), nullable=False)
#     funderContactEmail = db.Column(db.String(50), default='NULL')
#     funderContactPhoneNo = db.Column(db.String(12), default='NULL')
#     funderStreet = db.Column(db.String(50), default='NULL')
#     funderCity = db.Column(db.String(50), default='NULL')
#     funderState = db.Column(db.String(2), default='KY')
#     funderZipcode = db.Column(db.String(12), nullable=False)
#     UniqueConstraint(funderID)

#     def __repr__(self):
#         return " {} {}".format(self.funderID,  self.funderLink)


# # resultFarmer = Farmer.query.all()
# # resultFood = Food.query.all()
# # resultAuction = Auction.query.all()
# # resultFoodBank = FoodBank.query.all()
# resultFunder = Funder.query.all()
# #print (resultFarmer)
# #print (resultFood)
# #print (resultAuction)
# #print (resultFoodBank)
# print (resultFunder)
=======
    foreignKeyFood = db.relationship(
        'PurchasedProduce', back_populates='food_ID')
    UniqueConstraint(foodID, foodName)

    def __repr__(self):
        return " {} {}".format(self.foodID,  self.foodType)


class Auction(db.Model):
    __tablename__ = 'Auction'
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
    foreignKeyAuction = db.relationship(
        'Invoices', back_populates='auction_ID')
    UniqueConstraint(auctionID)

    def __repr__(self):
        return " {} {}".format(self.auctionID,  self.auctionDate)


class FoodBank(db.Model):
    __tablename__ = 'FoodBank'
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
    foreignKeyFoodBank = db.relationship(
        'Invoices', back_populates='foodBank_ID')
    UniqueConstraint(foodbankID, fbPhoneNo)

    def __repr__(self):
        return " {} {}".format(self.foodbankID,  self.fbName)


class Funder(db.Model):
    __tablename__ = 'Funder'
    funderID = db.Column(db.Integer, nullable=False, primary_key=True)
    funderLink = db.Column(db.String(50), nullable=False)
    funderContactName = db.Column(db.String(50), nullable=False)
    funderContactEmail = db.Column(db.String(50), default='NULL')
    funderContactPhoneNo = db.Column(db.String(12), default='NULL')
    funderStreet = db.Column(db.String(50), default='NULL')
    funderCity = db.Column(db.String(50), default='NULL')
    funderState = db.Column(db.String(2), default='KY')
    funderZipcode = db.Column(db.String(12), nullable=False)
    UniqueConstraint(funderID)
    foreignKeyFunder = db.relationship('Grant', back_populates='funder_ID')

    def __repr__(self):
        return " {} {}".format(self.funderID,  self.funderLink)


class Grant(db.Model):
    __tablename__ = 'Grant'
    grantID = db.Column(db.Integer, nullable=False, primary_key=True)
    funderID = db.Column(db.Integer, db.ForeignKey('Funder.funderID'))
    totalAward = db.Column(db.Float, nullable=False)
    totalBudgetUsed = db.Column(db.Float, default='NULL')
    startDate = db.Column(db.Date, default='NULL')
    endDate = db.Column(db.Date, default='NULL')
    restrictions = db.Column(db.String(1000), default='NULL')
    reportingRequirement = db.Column(db.String(1000), default='NULL')
    recordRequirement = db.Column(db.String(1000), default='NULL')
    closed = db.Column(default='NULL')
    programName = db.Column(db.String(50), default='NULL')
    grantType = db.Column(db.String(45), default='grant_type')
    foreignKeyGrant = db.relationship('Invoices', back_populates='grant_ID')
    UniqueConstraint(grantID)
    TINYINT(closed)
    funder_ID = db.relationship("Funder", back_populates="foreignKeyFunder")

    def __repr__(self):
        return " {} {}".format(self.grantID,  self.totalAward)


class PurchasedProduce(db.Model):
    __tablename__ = 'PurchasedProduce'
    pfID = db.Column(db.Integer, nullable=False, primary_key=True)
    foodID = db.Column(db.Integer, db.ForeignKey(
        'Food.foodID'), default='NULL')  # need to make this foreign key
    quantity = db.Column(db.Integer, nullable=False)
    unitPrice = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    foreignKeyPurchasedproduce = db.relationship(
        'Invoices', back_populates='purchasedProduce_ID')
    UniqueConstraint(pfID)
    food_ID = db.relationship("Food", back_populates="foreignKeyFood")

    def __repr__(self):
        return " {} {}".format(self.pfID,  self.quantity)


class Invoices(db.Model):
    __tablename__ = 'Invoices'
    invoiceNo = db.Column(db.Integer, nullable=False, primary_key=True)
    invoiceType = db.Column(db.String(50), nullable=False)
    outsideInvoice = db.Column(db.String(50), nullable=False)
    dateReceived = db.Column(db.Date, nullable=False)
    datePaid = db.Column(db.Date, nullable=False)
    totalPound = db.Column(db.Float, nullable=False)
    totalCost = db.Column(db.Float, nullable=False)
    checkNo = db.Column(db.Integer, default='NULL')
    deliveryFee = db.Column(db.Float, default='NULL')
    buyFee = db.Column(db.Float, default='NULL')
    purchaseOrder = db.Column(db.String(255), default='NULL')
    pfID = db.Column(db.Integer, db.ForeignKey(
        'PurchasedProduce.pfID'), default='NULL')
    grantID = db.Column(db.Integer, db.ForeignKey(
        'Grant.grantID'), default='NULL')
    farmerID = db.Column(db.Integer, db.ForeignKey(
        'Farmer.farmerID'), default='NULL')
    auctionID = db.Column(db.Integer, db.ForeignKey(
        'Auction.auctionID'), default='NULL')
    foodBankID = db.Column(db.Integer, db.ForeignKey(
        'FoodBank.foodbankID'), default='NULL')
    purchasedProduce_ID = db.relationship(
        "PurchasedProduce", back_populates="foreignKeyPurchasedproduce")
    grant_ID = db.relationship("Grant", back_populates="foreignKeyGrant")
    farmer_ID = db.relationship("Farmer", back_populates="foreignKeyFarmer")
    auction_ID = db.relationship("Auction", back_populates="foreignKeyAuction")
    foodBank_ID = db.relationship(
        "FoodBank", back_populates="foreignKeyFoodBank")
    UniqueConstraint(invoiceNo)

    def __repr__(self):
        return " {} {}".format(self.invoiceNo,  self.totalCost)


#resultFarmer = Farmer.query.all()
#resultFood = Food.query.all()
# resultAuction = Auction.query.all()
# resultFoodBank = FoodBank.query.all()
# resultFunder = Funder.query.all()
# resultGrant = Grant.query.all()
resultpurchasedProduce = PurchasedProduce.query.with_entities(
    PurchasedProduce.foodID, Food.foodType)
# resultInvoice = Invoices.query.all()
print(resultpurchasedProduce)
# print(resultInvoice)
# print(resultFunder)
# print (resultFarmer)
# print (resultFood)
# print (resultAuction)
# print (resultFoodBank)
# print (resultGrant)
>>>>>>> modelContinued
