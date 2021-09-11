from models import db, User, Post, Tag, PostTag
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for

def reset_database():
    db.drop_all()
    db.session.commit()
    db.create_all()
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

    tag1 = Tag(name='scary')
    tag2 = Tag(name='funny')
    tag3 = Tag(name='nerdy')
    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()

    alice_post1_tag3 = PostTag(post_id=1, tag_id=3)
    alice_post1_tag2 = PostTag(post_id=1, tag_id=2)
    bob_post1_tag3 = PostTag(post_id=2, tag_id=3)
    cate_post1_tag1 = PostTag(post_id=3, tag_id=1)
    cate_post2_tag1 = PostTag(post_id=4, tag_id=1)
    db.session.add_all([alice_post1_tag2, alice_post1_tag3, bob_post1_tag3, cate_post1_tag1, cate_post2_tag1])
    db.session.commit()

reset_database()
insert_data()

