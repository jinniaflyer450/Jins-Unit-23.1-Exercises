"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash, url_for
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

@app.route('/')
def redirect_home():
    return redirect('/users')

@app.route('/users')
def show_users():
    users = User.query.all()
    for user in users:
        if user.image_url == "no_image":
            user.image_url = url_for('static', filename='no_image.png')
            db.session.add(user)
            db.session.commit()
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
    if img_url != '':
        new_user = User(username=username, first_name=first_name, last_name=last_name, image_url =img_url)
    else:
        new_user = User(username=username, first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user_details(user_id):
    user = User.query.get(user_id)
    return render_template('userdetails.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user_details_form(user_id):
    user = User.query.get(user_id)
    return render_template('edituser.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edit_user_details(user_id):
    user = User.query.get(user_id)
    username = request.form['username']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['img-url']
    if username != '':
        user.username = username
    if first_name != '':
        user.first_name = first_name
    if last_name != '':
        user.last_name = last_name
    if img_url != '':
        user.image_url = img_url
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')