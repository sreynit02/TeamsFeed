from app import db


class Farmer(db.Model):
    __tablename__= 'Farmer'
    farmerID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f'Farmer {self.farmerID}'

resultlist = Farmer.query.all()
print(resultlist)
