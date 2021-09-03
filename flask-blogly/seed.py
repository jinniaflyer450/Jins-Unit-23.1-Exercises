from models import User, db
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for

def reset_database():
    db.drop_all()
    db.create_all()
    users = User.query.all()
    User.query.delete()
    db.session.commit()

def insert_data():
    alice = User(username='l33thacks', first_name='Alice', last_name = 'Johnson')
    bob = User(username='codingiscool30', first_name = 'Bob', last_name='Wu')
    cate= User(username='miraclewoman', first_name='Cate', last_name='Merriweather')
    db.session.add(alice)
    db.session.add(bob)
    db.session.add(cate)
    db.session.commit()

reset_database()
insert_data()

