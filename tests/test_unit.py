from flask_testing import TestCase
from application import app, db
from application.models import Chore
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        #Defines the flask object's configuration for the unit tests
        
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///', DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app
        
    def setUp(self):
        db.create_all()#create table schema
    
        chore = Chores(description="Test the application")  
        db.session.add(chore)
        db.session.commit()  

    def tearDown(self):
        #will be called after every test
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

class TestRead(TestBase):
    
    def test_read_chores(self):
        response = self.client.get(url_for("home"))
        self.assertIn("Test the application", str (response.data))

class TestCreate(TestBase):

    def test_create_chore(self):
        response = self.client.post(
        url_for("create_chore"),
        json={"description": "Add a new chore"},
        follow_redirects=True
        )
        
        new_chore = Chores.query.get(2)
        self.assertEqual("Add a new chore", new_chore.description)
  
    def test_create_chore_redirect(self):
        response = self.client.post(
        url_for("create_chore"),
        json={"description": "Add a new chore"},
        follow_redirects=True
        )
        self.assertIn("Add a new chore", str(response.data))