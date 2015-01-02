# test.py

import os
import unittest

from views import app, db
from config import basedir
from models import User

TEST_DB = 'test.db'


class AllTests(unittest.TestCase):
    # ###########################
    # ### setup and teardown ####
    # ###########################

    # execute prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # executed after to each test
    def tearDown(self):
        db.drop_all()

    # this function will be used to login
    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password), follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(name=name, password=password, email=email, confirm=confirm),
                             follow_redirects=True)

    # logout
    def logout(self):
        return self.app.get('logout', follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(name=name, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(name='Go to the bank', due_date='02/05/2014', priority='1',
                                               posted_date='02/04/2014', status='1'), follow_redirects=True)

    # each test should start with 'test'
    def test_user_setup(self):
        new_user = User("mherman", "michael@mherman.org", "michaelherman")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == 'mherman'

    # form is present on login page
    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)

    # test that un-registered users are unable to login
    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password.', response.data)

    # test that user can login
    def test_users_can_login(self):
        self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        response = self.login('Jean', 'pass')
        self.assertIn('You are logged in', response.data)

    # login with bad data
    def test_invalid_form_data(self):
        self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        response = self.login('JeanFail', 'passFaill')
        self.assertIn('Invalid username', response.data)

    # validate form is present in register page
    def test_form_is_present_on_register_page(self):
        response = self.app.get('register/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please register to start', response.data)

    # test if form is present and user already exist
    def test_user_registration(self):
        self.app.get('register/', follow_redirects=True)
        self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        self.app.get('register/', follow_redirects=True)
        response = self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        self.assertIn('already exist', response.data)

    # test logout functionality
    def test_logged_in_users_can_logout(self):
        self.register('Carlos', 'Carlos@test.com', 'pass', 'pass')
        self.login('Carlos', 'Pass')
        response = self.logout()
        self.assertIn('You are logged out', response.data)

    def test_not_logged_in_users_cannot_logout(self):
        response = self.logout()
        self.assertNotIn('You are logged out', response.data)

    # users can access to tasks
    def test_logged_in_users_can_access_tasks_page(self):
        self.register('Test', 'test@test.com', 'pass', 'pass')
        self.login('Test', 'pass')
        response = self.app.get('tasks/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Add a new task', response.data)

    def test_not_logged_in_users_cannot_access_task_page(self):
        response = self.app.get('tasks/', follow_redirects=True)
        self.assertIn("Please login first", response.data)

    def test_users_can_add_tasks(self):
        self.create_user('tester', 'tester@test.com', 'pass')
        self.login('tester', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn('New entry was successfully posted', response.data)

    def test_users_can_complete_tasks(self):
        self.create_user('JeanC', 'JeanC@test.com', 'pass')
        self.login('JeanC', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('complete/1/', follow_redirects=True)
        self.assertIn('marked as complete', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user('JeanC', 'JeanC@test.com', 'pass')
        self.login('JeanC', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('delete/1/', follow_redirects=True)
        self.assertIn('task was deleted', response.data)

    def test_users_cannot_complete_tasks_that_are_not_created_by_them(self):
        self.create_user('JeanC', 'JeanC@test.com', 'pass')
        self.login('JeanC', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.create_user('tester', 'tester@test.com', 'pass')
        self.login('tester', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('complete/1/', follow_redirects=True)
        self.assertNotIn('marked as complete', response.data)



if __name__ == "__main__":
    unittest.main()