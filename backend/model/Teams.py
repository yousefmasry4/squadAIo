import uuid
import datetime

from model import app, db, bcrypt


class Teams(db.Model):
    __tablename__ = "Teams"

    team_id = db.Column(db.String, primary_key=True)
    team_name = db.Column(db.String, nullable=False, unique=True)
    team_description = db.Column(
            db.String,
            nullable=False,
        )
    # team members are a users
    team_members = db.relationship('User', backref='team', lazy=True)
    # team leader
    team_leader = db.Column(db.String, db.ForeignKey('User.user_id'), nullable=False)
    # team order
    team_order= db.Column(db.Integer, nullable=True)
    # selected challenge for the team
    challenge_id = db.Column(db.String, db.ForeignKey('challenges.challenge_id'), nullable=True)
    challenge = db.relationship('challenges', backref=db.backref('teams', lazy=True))
    # hackathon
    hackathon_id = db.Column(db.String, db.ForeignKey('Hackathon.hackathon_id'), nullable=False)
    hackathon = db.relationship('Hackathon', backref=db.backref('teams', lazy=True))
    # CodeSubmissions
    code_submissions = db.relationship('CodeSubmission', backref='team', lazy=True)
    

    def __init__(self, team_name, team_description, team_leader, team_order, challenge_id, hackathon_id):
        self.team_name = team_name
        self.team_description = team_description
        self.team_leader = team_leader
        self.team_order = team_order
        self.challenge_id = challenge_id
        self.hackathon_id = hackathon_id
        self.team_id = uuid.uuid4()