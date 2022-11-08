from . import db # will only work once db is imported inside __init__.py
from flask_login import UserMixin #helps with user login
from sqlalchemy.sql import func

#database related classes
class Note(db.Model): #gets notes for each user
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000)) #note can be max 10000 characters
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #get info on timezone
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #store id of user who created the note, one to many relationship
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) #unique makes sure that no email repeat
    password= db.Column(db.String(150))
    username= db.Column(db.String(150))
    notes = db.relationship('Note') #list that stores all different notes. Able to access all notes that a user makes


