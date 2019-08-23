
import unittest
import os
import json
from ..app import create_app,db
class UsersTest(unittest.TestCase):
  """
  Users Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.user = {
      'pseudo': 'john',
      'mail': 'john.doe@john.com',
      'password': 'john'
    }

    with self.app.app_context():
      # create all tables
      db.create_all()
  
  def test_user_creation(self):
    """ test user creation with valid credentials """
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertTrue(json_data.get('jwt_token'))
    self.assertEqual(res.status_code, 201)

  def test_user_creation_with_existing_email(self):
    """ test user creation with already existing email"""
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_user_creation_with_no_password(self):
    """ test user creation with no password"""
    user1 = {
      'pseudo': 'john',
      'mail': 'john.doe@john.com'
    }
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_user_creation_with_no_email(self):
    """ test user creation with no email """
    user1 = {
      'pseudo': 'john',
      'pasword': 'john.doe@john.com'
    }
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertTrue(json_data.get('error'))

  def test_user_creation_with_empty_request(self):
    """ test user creation with empty request """
    user1 = {}
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
  
  def test_user_login(self):
    """ User Login Tests """
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    json_data = json.loads(res.data)
    self.assertTrue(json_data.get('jwt_token'))
    self.assertEqual(res.status_code, 200)

  def test_user_login_with_invalid_password(self):
    """ User Login Tests with invalid credentials """
    user1 = {
      'password': 'olawale',
      'mail': 'john.doe@john.com',
    }
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertFalse(json_data.get('jwt_token'))
    self.assertEqual(json_data.get('error'), 'invalid credentials')
    self.assertEqual(res.status_code, 400)

  def test_user_login_with_invalid_email(self):
    """ User Login Tests with invalid credentials """
    user1 = {
      'password': 'john',
      'email': 'olawale1111@mail.com',
    }
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    res = self.client().post('/api/v1/users/login', headers={'Content-Type': 'application/json'}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertFalse(json_data.get('jwt_token'))
    self.assertEqual(json_data.get('error'), 'you need valid email and or password to sign in')
    self.assertEqual(res.status_code, 403)

  def test_user_get_me(self):
    """ Test User Get Me """
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    api_token = json.loads(res.data).get('jwt_token')
    res = self.client().get('/api/v1/users/me', headers={'Content-Type': 'application/json', 'api-token': api_token})
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('mail'), 'john.doe@john.com')
    self.assertEqual(json_data.get('pseudo'), 'john')

  def test_user_update_me(self):
    """ Test User Update Me """
    user1 = {
      'pseudo': 'new name'
    }
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    api_token = json.loads(res.data).get('jwt_token')
    res = self.client().put('/api/v1/users/me/update', headers={'Content-Type': 'application/json', 'api-token': api_token}, data=json.dumps(user1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(json_data.get('pseudo'), 'new name')

  def test_delete_user(self):
    """ Test User Delete """
    res = self.client().post('/api/v1/users/create', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
    self.assertEqual(res.status_code, 201)
    api_token = json.loads(res.data).get('jwt_token')
    res = self.client().delete('/api/v1/users/me/delete', headers={'Content-Type': 'application/json', 'api-token': api_token})
    self.assertEqual(res.status_code, 204)
    
  def tearDown(self):
    """
    Tear Down
    """
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__ == "__main__":
  unittest.main() 