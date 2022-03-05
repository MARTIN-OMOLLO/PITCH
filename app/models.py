from. import db.login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import Usermixin


class User(Usermixin,db,model):

    __tablename__='users'

    id = db.column(db.integer,primary_key = True)
    username = db.column(db.string(255), unique = True, nullable = False)
    email =  db.column(db.string(255), unique = True, nullable = False)
    secure_password = db.column(db.string(255), nullable = False)


