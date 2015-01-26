# test.py

import os
import unittest

from datetime import date
from project import app, db, bcrypt
from config import basedir
from project.models import User, Task

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
        self.assertEquals(app.debug, False)

    # executed after to each test
    def tearDown(self):
        db.drop_all()

    # this function will be used to login
    def login(self, name, password):
        return self.app.post('/users/', data=dict(name=name, password=password),
                             follow_redirects=True)

    def register(self, name, email, password, confirm):
        return self.app.post('users/register/', data=dict(name=name, password=password, email=email, confirm=confirm),
                             follow_redirects=True)

    # logout
    def logout(self):
        return self.app.get('users/logout', follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(name=name, password=bcrypt.generate_password_hash(password), email=email)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('tasks/add/', data=dict(name='Go to the bank', due_date='02/05/2014', priority='1',
                                                     posted_date='02/04/2014', status='1'), follow_redirects=True)

    def create_admin_user(self):
        new_user = User(name='Super', email='super@test.com',
                        password=bcrypt.generate_password_hash('pass'), role='admin')
        db.session.add(new_user)
        db.session.commit()

    # each test should start with 'test'
    def test_user_setup(self):
        new_user = User("test", "test@testing.org", "pass")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == 'test'

    # form is present on login page

    def add_tasks(self):
        db.session.add(Task("Run around in circles", date(2015, 1, 22), 10, date(2015, 1, 05), 1, 1))
        db.session.commit()
        db.session.add(Task("My test task", date(2015, 7, 22), 10, date(2015, 9, 05), 1, 1))
        db.session.commit()

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please sign in to access your task list', response.data)

    # test that un-registered users are unable to login
    def test_users_cannot_login_unless_registered(self):
        response = self.login('asdasd', 'asdasd')
        self.assertIn('Invalid username or password.', response.data)

    # test that user can login
    def test_users_can_login(self):
        self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        response = self.login('Jean', 'pass')
        self.assertIn('You have logged in', response.data)

    # login with bad data
    def test_invalid_form_data(self):
        self.register('Jean', 'jean.guzman@ceroic.com', 'pass', 'pass')
        response = self.login('JeanFail', 'passFaill')
        self.assertIn('Invalid username', response.data)

    # validate form is present in register page
    def test_form_is_present_on_register_page(self):
        response = self.app.get('users/register/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please register to start', response.data)

    # test if form is present and user already exist
    def test_user_registration(self):
        self.register('Carlos', 'Carlos@test.com', 'pass', 'pass')
        response = self.register('Carlos', 'Carlos@test.com', 'pass', 'pass')
        self.assertIn('already exist', response.data)

    # test logout functionality
    def test_logged_in_users_can_logout(self):
        self.register('Carlos', 'Carlos@test.com', 'pass', 'pass')
        self.login('Carlos', 'pass')
        response = self.logout()
        self.assertIn('You have logged out', response.data)

    def test_not_logged_in_users_cannot_logout(self):
        response = self.logout()
        self.assertNotIn('You are logged out', response.data)

    # users can access to tasks
    def test_logged_in_users_can_access_tasks_page(self):
        self.register('Test', 'test@test.com', 'pass', 'pass')
        response = self.login('Test', 'pass')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Add a new task', response.data)

    def test_not_logged_in_users_cannot_access_task_page(self):
        response = self.app.get('tasks/tasks', follow_redirects=True)
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
        self.app.get('tasks/tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('tasks/complete/1/', follow_redirects=True)
        self.assertIn('marked as complete', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user('JeanC', 'JeanC@test.com', 'pass')
        self.login('JeanC', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get('tasks/delete/1/', follow_redirects=True)
        self.assertIn('task was deleted', response.data)

    def test_user_registration_field_error(self):
        response = self.register('Test', 'test@test.com', 'pass', '')
        self.assertIn('This field is required', response.data)

    def test_users_cannot_complete_tasks_that_are_not_created_by_them(self):
        self.create_user('JeanCA', 'JeanC@test.com', 'pass')
        self.login('JeanCA', 'pass')
        self.create_task()
        self.logout()
        self.create_user('CarlosA', 'Carlos@test.com', 'pass')
        self.login('CarlosA', 'pass')
        self.app.get('tasks/tasks/', follow_redirects=True)
        response = self.app.get('tasks/complete/1/', follow_redirects=True)
        self.assertIn('You can only update tasks that belong to you.', response.data)

    def test_users_cannot_delete_tasks_that_are_not_created_by_them(self):
        self.create_user('JeanCA', 'JeanC@test.com', 'pass')
        self.login('JeanCA', 'pass')
        self.create_task()
        self.logout()
        self.create_user('CarlosA', 'Carlos@test.com', 'pass')
        self.login('CarlosA', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('tasks/delete/1/', follow_redirects=True)
        self.assertIn('You can only delete tasks that belong to you.', response.data)

    def test_default_user_roles(self):
        db.session.add(User("Teste", "tester@test.com", "pass"))
        db.session.commit()
        users = db.session.query(User).all()
        print users
        for user in users:
            self.assertEquals(user.role, 'user')

    def test_admin_users_can_complete_tasks_that_are_not_created_by_them(self):
        self.create_user('JeanCA', 'JeanC@test.com', 'pass')
        self.login('JeanCA', 'pass')
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Super', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('complete/1/', follow_redirects=True)
        self.assertNotIn("You can only update tasks that belong to you.", response.data)

    def test_admin_users_can_delete_tasks_that_are_not_created_by_them(self):
        self.create_user('JeanCA', 'JeanC@test.com', 'pass')
        self.login('JeanCA', 'pass')
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Super', 'pass')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get('delete/1/', follow_redirects=True)
        self.assertNotIn("You can only delete tasks that belong to you.", response.data)

    def test_task_template_displays_logged_in_user_name(self):
        self.register('test', 'test@test.com', 'pass', 'pass')
        self.login('test', 'pass')
        response = self.app.get('tasks/tasks/', follow_redirects=True)
        self.assertIn('test', response.data)

    def test_users_cannot_see_task_modify_links_for_tasks_not_created_by_them(self):
        self.create_user('test', 'test@test.com', 'pass')
        self.login('test', 'pass')
        self.app.get('tasks/tasks', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register('testing', 'testing@test.com', 'pass', 'pass')
        response = self.login('testing', 'pass')
        self.assertNotIn('Mark as Complete', response.data)
        self.assertNotIn('Delete', response.data)

    def test_users_can_see_task_modify_links_for_tasks_created_by_them(self):
        self.create_user('test', 'test@test.com', 'pass')
        self.login('test', 'pass')
        self.app.get('tasks/tasks', follow_redirects=True)
        self.create_task()
        self.logout()
        self.register('testing', 'testing@test.com', 'pass', 'pass')
        self.login('testing', 'pass')
        response = self.create_task()
        self.assertIn('tasks/complete/2/', response.data)
        self.assertIn('tasks/complete/2/', response.data)

    def test_admin_users_can_see_task_modify_links_for_all_tasks(self):
        self.create_user('test', 'test@test.com', 'pass')
        self.login('test', 'pass')
        self.app.get('tasks/tasks', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_admin_user()
        self.login('Super', 'pass')
        self.app.get('tasks/tasks', follow_redirects=True)
        response = self.create_task()
        self.assertIn('tasks/complete/1/', response.data)
        self.assertIn('tasks/delete/1/', response.data)
        self.assertIn('tasks/complete/2/', response.data)
        self.assertIn('tasks/delete/2/', response.data)

    def test_404_error(self):
        response = self.app.get('/something')
        self.assertEquals(response.status_code, 404)
        self.assertIn('Sorry, not found', response.data)

    # def test_505_error(self):
    #     bad_user = User(name='broken', email='broken@broke.com', password='pass')
    #     db.session.add(bad_user)
    #     db.session.commit()
    #     response = self.login('broken', 'pass')
    #     self.assertEquals(response.status_code, 500)
    #     self.assertNotIn('ValueError: Invalid salt', response.data)
    #     self.assertIn('Something went wrong', response.data)

    def test_collection_endpoint_returns_correct_data(self):
        self.add_tasks()
        response = self.app.get('api/tasks/', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('Run around in circles', response.data)

    def test_resource_endpoint_returns_correct_data(self):
        self.add_tasks()
        response = self.app.get('api/tasks/2', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('My test task', response.data)
        self.assertNotIn('Run around in circles', response.data)

    def test_invalid_resource_endpoint_returns_error(self):
        self.add_tasks()
        response = self.app.get('api/tasks/20', follow_redirects=True)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn('Element does not exist', response.data)

if __name__ == "__main__":
    unittest.main()