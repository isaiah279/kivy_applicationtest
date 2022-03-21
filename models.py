from.import db
from sqlalchemy.sql import func
from flask_login import UserMixin
class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(100000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    #to associate notes with users
    user_id=db.Column(db.ForeignKey('user.id'))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    notes=db.relationship('Note')