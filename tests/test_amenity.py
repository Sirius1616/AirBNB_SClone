import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up an instance of Amenity for testing"""
        self.amenity = Amenity()
    
    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)
    
    def test_attributes(self):
        """Test if Amenity has the correct attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")
    
    def test_instance_creation(self):
        """Test if Amenity can be instantiated correctly"""
        self.assertIsInstance(self.amenity, Amenity)
    
    def test_attribute_assignment(self):
        """Test if attributes can be assigned correctly"""
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

if __name__ == "__main__":
    unittest.main()
