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

    def __init__(self, username, password, email, name,user_type='user', mobile=None,title=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode('utf-8')
        self.referral_code = uuid.uuid4()
        self.username = username
        self.user_type = user_type
        if user_type == 'user' and mobile is None:
            raise ValueError('Mobile number is required for user type')
        if user_type == 'user' and title is None:
            raise ValueError('Title is required for user type')
        self.name = name
        self.registered_on = datetime.datetime.now()
