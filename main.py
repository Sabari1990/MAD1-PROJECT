from flask import Flask, render_template as rt
from model import *
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///"+\
os.path.join(current_dir,"Database.sqlite3")

db.init_app(app)
app.app_context().push()

app.route('/', methods=['GET','POST'])
def home():
    return rt('home.html')

app.route('/sqldemo', methods=['GET','POST'])
def sqldemo():
    data = users.query.all()
    for i in data:
        print(i)
        return"sql_demo check vs_code terminal for output"
    

if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')