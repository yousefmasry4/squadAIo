import uuid
from model import app, db, bcrypt


class Teams(db.Model):
    __tablename__ = "Teams"

    team_id = db.Column(db.String, primary_key=True)
    team_name = db.Column(db.String, nullable=False, unique=True)
    team_description = db.Column(
            db.String,
            nullable=False,
        )
    # chalnge: chalnge has many teams but team can select only one chalnge
    challenge_id = db.Column(db.String, db.ForeignKey('challenges.challenge_id'), nullable=True)
    challenge = db.relationship('challenges', backref=db.backref('teams-challenges', lazy=True))
    # team members, team contain list of users
    team_members = db.relationship('User', backref=db.backref('teams-User', lazy=True), lazy=True)

    # team leader
    team_leader = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
    # team order
    team_order= db.Column(db.Integer, nullable=True)
    # CodeSubmissions: team has only one code submissions
    code_submissions = db.relationship('CodeSubmission', backref=db.backref('teams-CodeSubmission', lazy=True))

    # hackathon: hackathon has many teams
    hackathon_id = db.Column(db.String, db.ForeignKey('Hackathon.hackathon_id'), nullable=True)
    hackathon = db.relationship('Hackathon', backref=db.backref('teams-Hackathon', lazy=True))

    def __init__(self, team_name, team_description, team_leader, hackathon_id, challenge_id=None , team_order=None, code_submissions=None):
        self.team_name = team_name
        self.team_description = team_description
        self.challenge_id = challenge_id
        self.team_leader = team_leader
        print(self.team_name, self.team_description, self.challenge_id, self.team_leader, self.hackathon_id, self.team_order, self.code_submissions, self.team_id)

        self.hackathon_id = hackathon_id
        self.team_order = team_order
        self.code_submissions = code_submissions
        self.team_id = uuid.uuid4()
        # print all

    def to_dict(self):
        return {
            'team_id': self.team_id,
            'team_name': self.team_name,
            'team_description': self.team_description,
            'challenge_id': self.challenge_id,
            'team_leader': self.team_leader,
            'team_order': self.team_order,
            'code_submissions': [code_submission.to_dict() for code_submission in self.code_submissions],
            'hackathon_id': self.hackathon_id,
            # 'team_members': [team_member.to_dict() for team_member in self.team_members]
        }
