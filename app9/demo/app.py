from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre1234@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://bpkmpuxoskubtp:f98400c5f496531c2eff60678c2673b53101fdb71162894f1d8907fb4402cd82@ec2-3-229-210-93.compute-1.amazonaws.com:5432/db358j0mer2i66?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success/", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height) # creates a db.Model object
            db.session.add(data)
            db.session.commit()
            # calculate an average
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
        else:    
            return render_template("index.html", text="This email address is already used! Please try another one.")

@app.route("/success_file/", methods=['POST'])
def success_file():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        file.save(secure_filename("uploaded_"+file.filename))
        with open("uploaded_"+file.filename, "a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html", btn="download.html")

@app.route("/download/")
def download():
    return send_file("uploaded_"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug = True
    app.run() # port 5000