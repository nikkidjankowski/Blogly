from unittest import TestCase
from app import app
from flask import session
from models import db, connect_db, User

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_redirect(self):
        with app.test_client() as client:
            resp = client.get("/user")

            self.assertEqual(resp.status_code, 302)
    follow_redirects=True
    
    def test_route(self):
        with app.test_client() as client:
            resp = client.get('/newuser')
            html = resp.get_data(as_text=True)
            #self.assertEqual(resp.status_code, 200)
            #self.assertIn('<h1>Create a New User</h1>', html)

    def test_submit(self):
        with app.test_client() as client:
            resp = client.post('/user/newuser', 
                                data={'first_name': 'Paul', 'last_name': 'Ross', 'image_url': 'https://ctd-thechristianpost.netdna-ssl.com/en/full/52157/prison-break-season-5.jpg?w=760&h=507&l=50&t=40'})
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)


