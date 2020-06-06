import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'Mangoes')

    def test_password_setter(self): #ascertains that when password is being hashed and the pass_secure contains a value
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError): #raise attribute error when we try to access the password property
                self.new_user.password

    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('Mangoes'))