from app.models import User
from app import db
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user=User(password='denis')

    def test_password_hash(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_verify_password(self):
        self.assertTrue(self.new_user.verify_password('denis'))