import uuid
import datetime

from model import app, db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False)
    referral_code = db.Column(db.String, nullable=False, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    redeemed_referral_code = db.Column(db.String, nullable=True)
    user_type = db.Column(
        db.String,
        nullable=False,
        # user types: user, admin, super_admin
        server_default='user'
        )
    last_logged_in = db.Column(db.DateTime, nullable=True)
    last_logged_out = db.Column(db.DateTime, nullable=True)

    # one user only in one team
    team = db.relationship('Teams', backref=db.backref('users-Teams', lazy=True,uselist=False))

    # one user only can score code 
    code_submission_id = db.Column(db.String, db.ForeignKey('CodeSubmission.code_submission_id'), nullable=True)
    code_submission = db.relationship('CodeSubmission', backref=db.backref('users-CodeSubmission', lazy=True))


    def __init__(self, username, password, email, name,user_type='user', mobile=None,title=None, redeemed_referral_code=None, team_id=None, code_submission_id=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.email = email
        self.mobile = mobile
        self.title = title
        self.name = name
        self.referral_code = uuid.uuid4()
        self.redeemed_referral_code = redeemed_referral_code
        self.user_type = user_type
        self.registered_on = datetime.datetime.now()
        self.last_logged_in = None
        self.last_logged_out = None
        self.team_id = team_id
        self.code_submission_id = code_submission_id
        if user_type == 'user' and mobile is None:
            raise ValueError('Mobile number is required for user type')
        if user_type == 'user' and title is None:
            raise ValueError('Title is required for user type')
    def __repr__(self):
        return f'<username: {self.username} email: {self.email} name: {self.name} user_type: {self.user_type}'

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'mobile': self.mobile,
            'title': self.title,
            'name': self.name,
            'referral_code': self.referral_code,
            'registered_on': self.registered_on,
            'redeemed_referral_code': self.redeemed_referral_code,
            'user_type': self.user_type,
            'last_logged_in': self.last_logged_in,
            'last_logged_out': self.last_logged_out,
            'team_id': self.team_id,
            'code_submission_id': self.code_submission_id
        }