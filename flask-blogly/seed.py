from models import User, Post, db
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
    db.session.add_all([alice, bob, cate])
    db.session.commit()

    alice_post1 = Post(title='L33t hackz', content='Here are some l33t hacks--turn it off and back on.', user_id=1)
    bob_post1 = Post(title='Coding is cool!', content="I love coding because it's cool!", user_id=2)
    cate_post1 = Post(title='How to get rid of stalkers?', content="I have a stalker. Help?", user_id=3)
    cate_post2 = Post(title='Never mind...', content='I have bigger problems now.', user_id=3)
    db.session.add_all([alice_post1, bob_post1, cate_post1, cate_post2])
    db.session.commit()

reset_database()
insert_data()

