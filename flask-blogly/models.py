"""Models for Blogly."""
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

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
