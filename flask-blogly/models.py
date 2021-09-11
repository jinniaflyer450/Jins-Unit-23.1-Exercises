"""Models for Blogly."""
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """A user of the Blogly site."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(30), nullable = False, unique = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(30))
    image_url = db.Column(db.String(50), default="no_image")

    posts = db.relationship('Post', backref='user')


class Post(db.Model):
    """A post on the Blogly site."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(10000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Tag(db.Model):
    """A tag on posts on the Blogly site."""

    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)

    posts = db.relationship('Post', secondary='posts_tags', backref='tags')
    
class PostTag(db.Model):
    """A model of the relationship between tags and posts on the Blogly site."""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)