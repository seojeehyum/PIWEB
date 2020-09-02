# -*- coding: utf-8 -*-
<<<<<<< HEAD
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shindalsoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

@app.route('/')
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']

        insertUser = Employee(username,email,tel)
=======
from gtts import gTTS
from playsound import playsound
from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///seojeehyum.db'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:///id@비밀번호'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

class Employee(db.Model):
    userid=db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel=db.Column(db.String(50))
    spot=db.Column(db.String(100))

    def __init__(self,username,email,tel,spot) :
        self.username = username
        self.email = email
        self.tel = tel
        self.spot = spot

@app.route('/')
def index():
    all_data=Employee.query.order_by(Employee.userid.desc()).all() #select * from employee
    
    return render_template("index.html",employee=all_data)

@app.route('/insert',methods=["POST"])
def insert():
    if request.method == "POST":
        username=request.form['username']
        email = request.form['email']
        tel = request.form['tel']
        spot = request.form['spot']

        insertUser = Employee(username,email,tel,spot)
>>>>>>> 67ba074ae5f59f993055871ff0e25a3c4b33bec5
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))
<<<<<<< HEAD

@app.route('/delete/<uid>')
def delete(uid):
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
=======
@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        updateUser = Employee.query.get(request.form.get('userid'))
        updateUser.username=request.form['username']
        updateUser.email=request.form['email']
        updateUser.tel=request.form['tel']
        updateUser.spot=request.form['spot']
        db.session.commit()

        return redirect(url_for('index'))
@app.route('/delete/<uid>')
def delete(uid):
    delUser=Employee.query.get(uid)
>>>>>>> 67ba074ae5f59f993055871ff0e25a3c4b33bec5
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

<<<<<<< HEAD
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee.query.get(request.form.get('userid'))
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

=======
@app.route('/search',methods=["POST"])
def search() :
    txtsearch=request.form['txtSearch']
    searchUser=Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template('index.html',employee=searchUser,txtSearch=txtsearch)

@app.route('/playmp3')
def playSound() :
    text="고양이가 소리를 내려고 합니다."
    filename="hellosmartcat.mp3"
    tts=gTTS(text=text,lang="ko")
    tts.save(filename)
    playsound(filename)
>>>>>>> 67ba074ae5f59f993055871ff0e25a3c4b33bec5
    return "고양이가 소리를 냈습니다."