from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class users(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key=True, autoincrement = True)
    name=db.Column(db.String)
    email= db.Column(db.String, unique=True)
    password=db.Column(db.String)
    user_type=db.Column(db.String)

class user_Service_relation(db.Model):
    __tablename__= 'user_theaters_relation'
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),primary_key=True)
    theater_id =db.Column(db.Integer,db.ForeignKey("theaters.id"),primary_key=True)
    


class Services(db.Model):
    __tablename__= 'Services'
    id= db.Column(db.Integer,primary_key=True, autoincrement = True)
    name=db.Column(db.String,unique=True)
    status = db.Column(db.Boolean, default = False)
    user_id= db.relationship('users',secondary='user_theaters_relation')

class movies(db.Model):
    __tablename__= 'movies'
    id= db.Column(db.Integer,primary_key=True, autoincrement = True)
    name=db.Column(db.String)
    email= db.Column(db.String, unique=True)
    password=db.Column(db.String)
    user_type=db.Column(db.String)