import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up an instance of State for testing"""
        self.state = State(name="California")
    
    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
    
    def test_attributes(self):
        """Test if State has the correct attributes"""
        self.assertTrue(hasattr(self.state, "name"))
    
    def test_attribute_values(self):
        """Test if attributes are assigned correctly"""
        self.assertEqual(self.state.name, "California")
    
    def test_instance_creation(self):
        """Test if State can be instantiated correctly"""
        self.assertIsInstance(self.state, State)
    
    def test_default_values(self):
        """Test default values when no attributes are provided"""
        state2 = State()
        self.assertEqual(state2.name, "")

if __name__ == "__main__":
    unittest.main()