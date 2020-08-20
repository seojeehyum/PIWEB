# -*- coding: utf-8 -*-
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
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))
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
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

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
    return "고양이가 소리를 냈습니다."