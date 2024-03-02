import uuid
import datetime

from model import app, db, bcrypt


class CodeSubmission(db.Model):
    __tablename__ = "CodeSubmission"
    # code submission id
    code_submission_id = db.Column(db.String, primary_key=True)
    # code submission date
    code_submission_date = db.Column(db.DateTime, nullable=False)
    # code submission file
    code_submission_file = db.Column(db.String, nullable=False)
    # code submission team 1:1
    team_id = db.Column(db.String, db.ForeignKey('Teams.team_id'), nullable=False)
    team = db.relationship('Teams', backref=db.backref('code_submissions-Teams', lazy=True))
    # score
    score = db.Column(db.Integer, nullable=True)
    # score by one user
    score_by = db.Column(db.String, nullable=True)
    

    def __init__(self, code_submission_date, code_submission_file, team_id, score=None, score_by=None):
        self.code_submission_date = code_submission_date
        self.code_submission_file = code_submission_file
        self.team_id = team_id
        self.score = score
        self.score_by = score_by
        self.code_submission_id = uuid.uuid4()

    def to_dict(self):
        return {
            'code_submission_id': self.code_submission_id,
            'code_submission_date': self.code_submission_date,
            'code_submission_file': self.code_submission_file,
            'team_id': self.team_id,
            'score': self.score,
            'score_by': self.score_by
        }
    