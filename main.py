from flask import Flask, render_template as rt
app = Flask(__name__)

app.route('/', methods=['GET','POST'])
def home():
    rt('home.html')
    

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')