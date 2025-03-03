import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up an instance of City for testing"""
        self.city = City(name="San Francisco", state_id="CA123")
    
    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)
    
    def test_attributes(self):
        """Test if City has the correct attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
    
    def test_attribute_values(self):
        """Test if attributes are assigned correctly"""
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA123")
    
    def test_instance_creation(self):
        """Test if City can be instantiated correctly"""
        self.assertIsInstance(self.city, City)
    
    def test_default_values(self):
        """Test default values when no attributes are provided"""
        city2 = City()
        self.assertEqual(city2.name, "")
        self.assertEqual(city2.state_id, "")

if __name__ == "__main__":
    unittest.main()