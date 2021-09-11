"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash, url_for
from models import db, connect_db, User, Post, Tag, PostTag
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

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    tags = Post.query.get(post_id).tags
    return render_template('postdetail.html', post=post, tags=tags)

@app.route('/users/<int:user_id>/posts/new')
def add_post_form(user_id):
    user = User.query.get(user_id)
    return render_template('addpost.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>/edit')
def edit_post_form(post_id):
    post = Post.query.get(post_id)
    return render_template('editpost.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    post = Post.query.get(post_id)
    title = request.form['title']
    content = request.form['content']
    post.title = title
    post.content = content
    db.session.add(post)
    db.session.commit()
    return redirect(f'/posts/{post_id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    user_id = post.user.id
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/tags')
def show_tag_list():
    tags = Tag.query.all()
    return render_template('taglist.html', tags = tags)

@app.route('/tags/<int:tag_id>')
def show_tag_details(tag_id):
    tag = Tag.query.get(tag_id)
    posts = tag.posts
    return render_template('tagdetails.html', tag=tag, posts=posts)

@app.route('/tags/new')
def new_tag_form():
    return render_template('newtag.html')

@app.route('/tags/new', methods=["POST"])
def add_new_tag():
    name=request.form["name"]
    new_tag=Tag(name=name)
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit')
def edit_tag_form(tag_id):
    tag=Tag.query.get(tag_id)
    return render_template('edittag.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def edit_tag(tag_id):
    tag=Tag.query.get(tag_id)
    name=request.form["name"]
    tag.name = name
    db.session.add(tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    tag=Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags')




