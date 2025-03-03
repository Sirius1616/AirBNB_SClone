import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up an instance of Place for testing"""
        self.place = Place()
    
    def test_instance_creation(self):
        """Test if the instance is correctly created"""
        self.assertIsInstance(self.place, Place)
    
    def test_attributes(self):
        """Test if Place attributes exist and have the correct default values"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
    
    def test_attribute_assignment(self):
        """Test assigning values to attributes"""
        self.place.city_id = "1234"
        self.place.user_id = "5678"
        self.place.name = "Luxury Apartment"
        self.place.description = "A beautiful place to stay."
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 150
        self.place.latitude = 12.3456
        self.place.longitude = -98.7654
        self.place.amenity_ids = ["wifi", "pool"]
        
        self.assertEqual(self.place.city_id, "1234")
        self.assertEqual(self.place.user_id, "5678")
        self.assertEqual(self.place.name, "Luxury Apartment")
        self.assertEqual(self.place.description, "A beautiful place to stay.")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 12.3456)
        self.assertEqual(self.place.longitude, -98.7654)
        self.assertEqual(self.place.amenity_ids, ["wifi", "pool"])

if __name__ == "__main__":
    unittest.main()