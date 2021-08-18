from models import User, db
from app import app
from flask_sqlalchemy import SQLAlchemy

db.drop_all()
db.create_all()

User.query.delete()

alice = User(username='l33thacks', first_name='Alice', last_name = 'Johnson')
bob = User(username='codingiscool30', first_name = 'Bob', last_name='Wu', image_url='angry_birds')
cate= User(username='miraclewoman', first_name='Cate', last_name='Merriweather')

db.session.add(alice)
db.session.add(bob)
db.session.add(cate)

db.session.commit()