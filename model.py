from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class users(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key=True, autoincrement = True)
    name=db.Column(db.String)
    email= db.Column(db.String, unique=True)
    password=db.Column(db.String)
    user_type=db.Column(db.String)

