import uuid
import datetime

from model import app, db, bcrypt


class Hackathon(db.Model):
    __tablename__ = "Hackathon"

    hackathon_id = db.Column(db.String, primary_key=True)
    hackathon_name = db.Column(db.String, nullable=False, unique=True)
    hackathon_theme = db.Column(
            db.String,
            nullable=False,
        )
    # regestration range
    reg_start = db.Column(db.DateTime, nullable=False)
    reg_end = db.Column(db.DateTime, nullable=False)
    # event date
    event_start = db.Column(db.DateTime, nullable=False)
    event_end = db.Column(db.DateTime, nullable=False)
    # challenges
    challenges = db.relationship('challenges', backref='hackathon', lazy=True)
    # teams
    teams = db.relationship('Teams', backref='hackathon', lazy=True)
    
    # prizes
    prizes = db.relationship('Price', backref='hackathon', lazy=True)

    def __init__(self, hackathon_name, hackathon_theme, reg_start, reg_end, event_start, event_end):
        self.hackathon_name = hackathon_name
        self.hackathon_theme = hackathon_theme
        self.reg_start = reg_start
        self.reg_end = reg_end
        self.event_start = event_start
        self.event_end = event_end
        self.hackathon_id = uuid.uuid4()

