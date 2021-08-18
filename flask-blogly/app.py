"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'catdog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ob1wankenobi@localhost/blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/new')
def add_user_form():
    return render_template('adduser.html')

@app.route('/users/new', methods=['POST'])
def add_user():
    username = request.form['username']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['img-url']
    new_user = User(username=username, first_name=first_name, last_name=last_name, image_url = img_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

