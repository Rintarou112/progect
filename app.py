from flask import Flask, render_template, request, url_for, flash, session, redirect, abort
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, TextAreaField
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import select
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "GDtfD^&$%@^8tgYjD"
csrf = CSRFProtect(app)

menu = [
    {"name": 'Главная', "url": "index"},
    {"name": 'Мои заметки', "url": "notes"},
    {"name": 'Создать заметку', "url": "new"}
        ]

class MyNote(FlaskForm):
    heading = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Note(db.Model):
    __tablename__="notes"
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(120))
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, heading, text):
        self.heading = heading
        self.text = text


@app.route("/index")
@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная страница', menu=menu)

@app.route("/notes")
def notes():
    print(url_for('notes'))
    data = Note.query.order_by(Note.date.desc()).all()
    
    return render_template('notes.html', title='Мои заметки', menu=menu, data=data)

@app.route("/new", methods=['POST', 'GET'])
def new():
    print(url_for('new'))
    #data = Note.query.paginate(page=1, per_page=5)
    data = Note.query.order_by(Note.date.desc()).limit(5)
    form = MyNote()
    if request.method == 'POST':
        if form.validate_on_submit():
            heading = form.data['heading']
            text = form.data['text']
            new_note = Note(heading, text)
            db.session.add(new_note)
            db.session.commit()
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('new.html', title='Создать заметку', menu=menu, form=form, data=data)

@app.route("/notes/<int:id>")
def delet(id):
    Note.query.filter_by(id=id).delete()
    try:
        db.session.commit()
        return redirect(url_for('notes'))
    except:
        return 'Ошибка'
    
@app.route("/notes/<int:id>/info")
def info(id):
    data = Note.query.filter_by(id=id).all()
    for i in data:
        name = i.heading
        
    return render_template('notes_info.html', title=name, menu=menu, data=data )
    
@app.route("/notes/<int:id>/update")
def update(id):
    data = Note.query.filter_by(id=id).all()
    for i in data:
        name = i.heading
    form = MyNote()
    
    return render_template('notes_update.html', title=name, menu=menu, data=data, form=form )
    
    

if __name__ == '__main__':
    app.run(debug=True)