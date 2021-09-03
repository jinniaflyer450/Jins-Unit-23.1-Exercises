from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, connect_db, User
from flask_sqlalchemy import SQLAlchemy
from app import app
from seed import reset_database, insert_data
from unittest import TestCase

class BloglyTests(TestCase):
    def setUp(self):
        """Sets up the tests by inserting three instances of the User class into the users table."""
        insert_data()
    
    @classmethod
    def setUpClass(cls):
        """Sets up the database before all tests"""
        reset_database()

    def tearDown(self):
        """Resets the database after each test."""
        reset_database()
    
    def test_show_users(self):
        """Tests if the 'show_users' view function returns 'index.html' with the users in the database in the template."""
        with app.test_client() as client:
            response = client.get('/users')
            self.assertEqual(response.status_code, 200)
            self.assertIn('<title>Blogly Homepage</title>', response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/1'>l33thacks</a></li>", response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/2'>codingiscool30</a></li>", response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/3'>miraclewoman</a></li>", response.get_data(as_text=True))
    
    def test_redirect_home(self):
        """Tests if the 'redirect_home' view function returns a redirect to 'index.html' with the users in the database displayed."""
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 302)
            self.assertIn('Redirecting', response.get_data(as_text=True))
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<title>Blogly Homepage</title>', response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/1'>l33thacks</a></li>", response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/2'>codingiscool30</a></li>", response.get_data(as_text=True))
            self.assertIn("<li><a href='/users/3'>miraclewoman</a></li>", response.get_data(as_text=True))
    
    def test_show_users_updates(self):
        """Tests to see if the url for the default user image stored on an instance of the User class is what it's supposed to be 
        before and after hitting the '/users' route."""
        with app.test_client() as client:
            user = User.query.get(1)
            self.assertEqual(user.image_url, "no_image")
            response = client.get('/users')
            user = User.query.get(1)
            self.assertEqual(user.image_url, url_for('static', filename='no_image.png'))
    
    def test_add_user_form(self):
        """Tests if the 'add_user_form' view function returns the form to add a new user for a get request."""
        with app.test_client() as client:
            response = client.get('/users/new')
            self.assertEqual(response.status_code, 200)
            self.assertIn('<title>Add New User</title>', response.get_data(as_text=True))
    
    def test_add_user_db(self):
        """Tests if the 'add_user' function successfully adds a user to the database when a post request with relevant data is made.
        """
        with app.test_client() as client:
            self.assertEqual(None, User.query.get(4))
            response = client.post('/users/new', data={"username": "psych9000", "first-name": "Wilhelm", "last-name": "Wundt", 
            "img-url": ""}, 
            follow_redirects=True)
            wilhelm = User.query.get(4)
            self.assertEqual(wilhelm.id, 4)
            self.assertEqual(wilhelm.first_name, "Wilhelm")
            self.assertEqual(wilhelm.last_name, "Wundt")
    

    def test_add_user_redirect(self):
        """Tests if the 'add_user' function returns a redirect to 'index.html' with the newest database addition to the list."""
        with app.test_client() as client:
            response = client.post('/users/new', data={"username": "psych9000", "first-name": "Wilhelm", "last-name": "Wundt", 
            "img-url": ""}, 
            follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("<li><a href='/users/4'>psych9000</a></li>", response.get_data(as_text=True))
    
    def test_show_user_details(self):
        """Tests if 'show_user_details' returns 'userdetails.html' with the user corresponding to the id in the URL."""
        with app.test_client() as client:
            response = client.get('/users/3')
            self.assertIn('<li>First Name: Cate</li>', response.get_data(as_text=True))
            self.assertIn('<li>Last Name: Merriweather</li>', response.get_data(as_text=True))



