from app import db

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(400))

    def __init__(self,row):
        self.row = row

    def __repr__(self):
        return '<id {}>'.format(self.id)

#This is known as inheritance
class SecondTable(db.Model): #<-
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.Float)

    def __init__(self, row):
        self.row = row
