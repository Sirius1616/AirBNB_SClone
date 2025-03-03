import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()
    
    def test_instance(self):
        """Test if the instance is correctly created"""
        self.assertIsInstance(self.review, Review)
    
    def test_default_attributes(self):
        """Test if default attributes are correctly set"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
    
    def test_attribute_assignment(self):
        """Test if attributes can be assigned values"""
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "Great place to stay!"
        
        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "Great place to stay!")

if __name__ == "__main__":
    unittest.main()