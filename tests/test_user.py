import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up an instance of User for testing"""
        self.user = User(email="test@example.com", password="securepass", first_name="John", last_name="Doe")
    
    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
    
    def test_attributes(self):
        """Test if User has the correct attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
    
    def test_attribute_values(self):
        """Test if attributes are assigned correctly"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "securepass")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
    
    def test_instance_creation(self):
        """Test if User can be instantiated correctly"""
        self.assertIsInstance(self.user, User)
    
    def test_default_values(self):
        """Test default values when no attributes are provided"""
        user2 = User()
        self.assertEqual(user2.email, "")
        self.assertEqual(user2.password, "")
        self.assertEqual(user2.first_name, "")
        self.assertEqual(user2.last_name, "")

if __name__ == "__main__":
    unittest.main()
