from . import db

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    age = db.Column(db.String(120))
    highest_score = db.Column(db.Integer)
    tdollars =  db.Column(db.Integer)
    image = db.Column(db.String(120))
    sex = db.Column(db.String(1))
    
    
    def __init__(self, firstname, lastname, age, image, sex, time):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.image = image
        self.sex = sex
        self.tdollars = 0
        self.created_on = time
        self.highest_score = 0

    def __repr__(self):
        return '<User %r>' % self.firstname
