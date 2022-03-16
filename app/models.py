from. import login_manager
from. import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):

    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    email =  db.Column(db.String(255), unique = True, nullable = False)
    secure_password = db.Column(db.String(255), nullable = False)
    bio = db.Column(db.String(255))

    comment =  db.relationship('Comment',backref='user',lazy='dynamic')
    upvote =  db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote =  db.relationship('Downvote',backref='user',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self,secure_password,password)
    def save_u(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()



