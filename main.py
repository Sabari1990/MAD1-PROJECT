from flask import Flask, render_template as rt,request
from model import *
import os
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///"+\
os.path.join(current_dir,"Database.sqlite3")

db.init_app(app)
app.app_context().push()

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        user_email = request.form['EMAIL']
        user_password = request.form['PASSWORD']

        user = users.query.filter_by(email = user_email).first()
       
        if user:
         if user_password == user.password:
             print('user exists')
             print(user.user_type)

        return"user exists,user.user_type"
    return rt('home.html')

@app.route('/admin', methods=['GET','POST'])
def admin():
    return rt('admin.html')

@app.route('/Customer', methods=['GET','POST'])
def Customer():
    return rt('Customer.html')

@app.route('/theater', methods=['GET','POST'])
def theater():
    return rt('theater.html')





@app.route('/sqldemo', methods=['GET','POST'])
def sqldemo():
    data = users.query.filter(users.user_type =='Customer', users.name.like("a%")).all()

    print('id','name','email','user_type')
    for i in data:
        print(i.id,i.name,i.email,i.user_type)
    return"sql_demo check vs_code terminal for output"
    
@app.route('/datashow', methods=['GET','POST'])
def datashow():
    data = users.query.filter(users.user_type =='Customer').all()
    return rt('data.html', var = data)

    

    


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')