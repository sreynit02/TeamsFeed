from app import db


class Farmer(db.Model):
    __tablename__ = 'Farmer'
    farmerID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return " {} {}".format(self.farmerID, self.firstName)

class Food(db.Model):
    __tablename__ = 'Food'
    foodID = db.Column(db.Integer, primary_key=True)
    foodType = db.Column(db.String(50), nullable=False, default='produce')
    foodName = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return " {} {}".format(self.foodID, self.foodType)



resultFarmer = Farmer.query.all()
resultFood = Food.query.all()
#print(resultFarmer)
print(resultFood)
