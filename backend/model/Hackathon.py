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
    # challenges : hackethon  has many challenges
    challenges = db.relationship('challenges', backref='hackathon-challenges', lazy=True)
    # prizes: hackethon  has many prizes
    prizes = db.relationship('Price', backref='hackathon-Price', lazy=True)
    # teams: hackethon  has many teams
    teams = db.relationship('Teams', backref='hackathon-Teams', lazy=True)

    def __init__(self, hackathon_name, hackathon_theme, reg_start, reg_end, event_start, event_end):
        self.hackathon_name = hackathon_name
        self.hackathon_theme = hackathon_theme
        self.reg_start = reg_start
        self.reg_end = reg_end
        self.event_start = event_start
        self.event_end = event_end
        self.hackathon_id = uuid.uuid4()

    def __repr__(self):
        return f"Hackathon('{self.hackathon_name}', '{self.hackathon_theme}', '{self.reg_start}', '{self.reg_end}', '{self.event_start}', '{self.event_end}')"
    def to_dict(self):
        return {
            'hackathon_id': self.hackathon_id,
            'hackathon_name': self.hackathon_name,
            'hackathon_theme': self.hackathon_theme,
            'reg_start': self.reg_start,
            'reg_end': self.reg_end,
            'event_start': self.event_start,
            'event_end': self.event_end,
            'challenges': [challenge.to_dict() for challenge in self.challenges],
            'prizes': [prize.to_dict() for prize in self.prizes],
            'teams': [team.to_dict() for team in self.teams]

        }

#     make it json serializable
    def to_json(self):
        return {
            'hackathon_id': self.hackathon_id,
            'hackathon_name': self.hackathon_name,
            'hackathon_theme': self.hackathon_theme,
            'reg_start': self.reg_start,
            'reg_end': self.reg_end,
            'event_start': self.event_start,
            'event_end': self.event_end,
            # 'challenges': [challenge.to_json() for challenge in self.challenges],
            # 'prizes': [prize.to_json() for prize in self.prizes],
            # 'teams': [team.to_json() for team in self.teams]

        }

    def to_json(self):
        return {
            'hackathon_id':str(self.hackathon_id),
            'hackathon_name': self.hackathon_name,
            'hackathon_theme': self.hackathon_theme,
            'reg_start': self.reg_start,
            'reg_end': self.reg_end,
            'event_start': self.event_start,
            'event_end': self.event_end,

        }
