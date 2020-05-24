from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary_key уникальность
    title = db.Column(db.String(100), nullable=False) #
    intro = db.Column(db.String(300), nullable=False) # статья не должна быть пустой, макс.длина 300
    text = db.Column( db.Text, nullable=False ) # для статьи, Текс для большого объема текста
    image = db.Column( db.String( 300 ), nullable=False )
    date = db.Column(db.DateTime, default=datetime.utcnow) # db.DateTime для даты; default ставит текущее время создания автоматом
    marker = db.Column( db.String( 30 ), nullable=False )


    def __repr__(self):
        return '<Article %r>' % self.marker # для запросов из бд, по умолчанию self.id, изменил для Главной страницы

class Literat(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column( db.DateTime, default=datetime.utcnow )

    def __repr__(self):
        return '<Literat %r>' % self.id


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    date = db.Column( db.DateTime, default=datetime.utcnow )

    def __repr__(self):
        return '<Literat %r>' % self.id


class Scrum(db.Model):
    id = db.Column( db.Integer, primary_key=True )
    scrum = db.Column(db.Text, nullable=False)
    date = db.Column( db.DateTime, default=datetime.utcnow )

    def __repr__(self):
        return '<Literat %r>' % self.id