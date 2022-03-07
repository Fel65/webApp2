from application import db

#represents the house table in database
class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    owner_email = db.Column(db.Boolean, nullable=False, default=False)
    date_added = db.Column(db.DateTime) 
    #chores_description = db.relationship('Chore', backref='house')

#represents the chores table in database
class Chore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chore_description = db.Column(db.String(255), nullable=False)
    charge = db.Column(db.Float, nullable=False, default=False)
    job_done = db.Column(db.String(25), nullable=False, default=False)
    #house_id = db.Column(db.Integer, db.ForeignKey('house.id'))