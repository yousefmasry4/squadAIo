import uuid
import datetime

from model import app, db, bcrypt


class Price(db.Model):
    __tablename__ = "Price"

    price_id = db.Column(db.String, primary_key=True)
    price_name = db.Column(db.String, nullable=False, unique=True)
    price_description = db.Column(
            db.String,
            nullable=False,
        )
    price_order = db.Column(db.Integer, nullable=False)
    
    hackathon_id = db.Column(db.String, db.ForeignKey('Hackathon.hackathon_id'), nullable=False)
    hackathon = db.relationship('Hackathon', backref=db.backref('prizes', lazy=True))

    def __init__(self, price_name, price_description, price_order, hackathon_id):
        self.price_name = price_name
        self.price_description = price_description
        self.price_order = price_order
        self.hackathon_id = hackathon_id
        self.price_id = uuid.uuid4()