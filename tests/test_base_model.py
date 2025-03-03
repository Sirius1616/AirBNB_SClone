import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if instance is correctly created."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """Test if each instance has a unique ID."""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_str_representation(self):
        """Test the string representation of the instance."""
        string_rep = str(self.model)
        self.assertIn("[BaseModel]", string_rep)
        self.assertIn(self.model.id, string_rep)

    def test_save_updates_updated_at(self):
        """Test if calling save updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertLess(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test if to_dict() method returns the correct dictionary representation."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_create_instance_from_dict(self):
        """Test if a new instance can be created using to_dict output."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertIsInstance(new_model, BaseModel)

if __name__ == "__main__":
    unittest.main()
