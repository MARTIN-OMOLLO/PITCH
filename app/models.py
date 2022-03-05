from. import db.login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import Usermixin


class User(Usermixin,db,model):

    __tablename__='users'

    id = db.column(db.integer,primary_key = True)
    username = db.column(db.string(255), unique = True, nullable = False)
    email =  db.column(db.string(255), unique = True, nullable = False)
    secure_password = db.column(db.string(255), nullable = False)
    bio = db.column(db.string(255))

    pitches = db.relationship('Pitch',brackef='user',lazy='dynamic')
    comment =  db.relationship('Comment',brackef='user',lazy='dynamic')
    upvote =  db.relationship('Upvote',brackef='user',lazy='dynamic')
    downvote =  db.relationship('Downvote',brackef='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self,secure_password,password)



