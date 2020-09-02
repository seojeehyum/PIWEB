import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcat.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
<<<<<<< HEAD
class LangAlarmConf(db.Model):
    __tablename__ = 'tblLangAlarmConf'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alarmtime = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    def __init__(self, alarmtime):
        self.alarmtime = alarmtime

=======
>>>>>>> b9c8b78407c419119e26f63d73d4148dd5e419ba

class LangAlarmWord(db.Model):
    __tablename__ = 'tblLangAlarmWord'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(30), unique=False, nullable=True)
    word = db.Column(db.String(100), unique=False, nullable=False)
    memo = db.Column(db.String(200), unique=False, nullable=True)
    cntplayed = db.Column(db.Integer, unique=False, nullable=True)
    useyn = db.Column(db.String(1), unique=False, nullable=True)
    regdate = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)

    def __init__(self, category, word, memo):
        self.category = category
        self.word = word
        self.memo = memo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def pages(page):
    return render_template('/pages/'+page)
    
@app.route('/contents/<page>')
def contents(page):
    return render_template('/contents/'+page)

<<<<<<< HEAD
@app.route('/bss/list.html')
def bbslist() :
    read_data = LangAlarmWord.query.all()
    return render_template('/bbs/list.html',lagnwords=read_data)

=======
>>>>>>> b9c8b78407c419119e26f63d73d4148dd5e419ba
@app.route('/bbs/<page>')
def bbs(page):
    all_data = LangAlarmWord.query.order_by(LangAlarmWord.id.desc()).all()
    return render_template('/bbs/'+page, langwords = all_data)

<<<<<<< HEAD
@app.route('/bbs_add.html', methods=['POST'])
def bbslistadd():
=======
@app.route('/bbs_insert', methods=['POST'])
def bbsinsert():
>>>>>>> b9c8b78407c419119e26f63d73d4148dd5e419ba
    category = request.form['category']
    word = request.form['word']
    memo = request.form['memo']
    newWord = LangAlarmWord(category,word,memo)
    db.session.add(newWord)
    db.session.commit()
    return "success"
