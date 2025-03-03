import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test if all() returns a dictionary"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(f"BaseModel.{self.obj.id}", objects)

    def test_new(self):
        """Test if new() correctly adds objects"""
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if save() correctly writes to file"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as f:
            data = json.load(f)
        self.assertIn(f"BaseModel.{self.obj.id}", data)

    def test_reload(self):
        """Test if reload() correctly loads data"""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(f"BaseModel.{self.obj.id}", new_storage.all())


if __name__ == "__main__":
    unittest.main()
