from flask import Flask, render_template as rt,request,redirect,url_for
from model import *
from sqlalchemy import and_ , or_
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
        Email = request.form['email']
        Password = request.form['password']

        user = users.query.filter_by(email = Email).first()
       
        if user:
           if Password == user.password:
              if user.user_type =='Server':
                  return redirect(url_for("Server_dashboard"))
              elif user.user_type == 'Customer':
                  return redirect(url_for("Customer_dashboard"))
              elif user.user_type == 'Admin':  
                  return redirect(url_for("Admin_dashboard"))
            
              return "user exists" 
           else:
             return "password is wrong"
        else:
             return rt('home.html', message='user does not exist')
       
    return rt('home.html')

@app.route('/userSignUp', methods=['GET','POST'])
def userSignUp():
    if request.method == 'POST':
       Email = request.form['email']
       Password = request.form['password']
       Username = request.form['name']
       UserType = request.form['user_type']
       newUser =users(name=Username, email=Email, password=Password,user_type=UserType)
       db.session.add(newUser)
       db.session.commit()
       return redirect(url_for("home"), message ="New User Created")
    return rt('userSignUp.html')


@app.route('/Customer_Dashboard', methods=['GET','POST'])
def Customer_dashboard():
    return rt('CustomerDashboard.html')
    
@app.route('/AdminDashboard', methods=['GET','POST'])
def Admin_dashboard():
    return rt('AdminDashboard.html')

@app.route('/ServerDashboard', methods=['GET','POST'])
def Server_dashboard():
    return rt('ServerDashboard.html')


@app.route('/Admin', methods=['GET','POST'])
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