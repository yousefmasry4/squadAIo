import uuid
import datetime

from model import app, db, bcrypt


class challenges(db.Model):
    __tablename__ = "challenges"

    challenge_id = db.Column(db.String, primary_key=True)
    challenge_name = db.Column(db.String, nullable=False, unique=True)
    challenge_description = db.Column(
            db.String,
            nullable=False,
        )
    
    
    hackathon_id = db.Column(db.String, db.ForeignKey('Hackathon.hackathon_id'), nullable=False)
    hackathon = db.relationship('Hackathon', backref=db.backref('challenges', lazy=True))

    def __init__(self, challenge_name, challenge_description, hackathon_id):
        self.challenge_name = challenge_name
        self.challenge_description = challenge_description
        self.hackathon_id = hackathon_id
        self.challenge_id = uuid.uuid4()
