"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLALchemy()

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
    image_url = db.Column(db.string(30), default = 'Insert_default_image_later')
