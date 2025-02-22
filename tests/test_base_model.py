#!/usr/bin/env python
"""Module to test the basemodel"""
from models.base_model import BaseModel
import unittest
import time
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """THe class that inherits methods from the unittest module"""

    def setUp(self):
        """Teardown method to be used be other test methods"""

        self.model = BaseModel()


    def test_instance_creation(self):
        """Test the created instance for the instance they belong to"""

        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    
    def test_unique_id(self):
        """Tests the id of differnt instances to show uniqueness"""

        self.model2 = BaseModel()

        self.assertNotEqual(self.model2.id, self.model.id)

    def test_str_method(self):
        expected_output = "[{}] ({}) {}".format('BaseModel',\
                                                 self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)
    
    def test_save(self):

        first_update = self.model.updated_at
        time.sleep(3)
        self.model.save()
        self.assertNotEqual(first_update, self.model.updated_at)
        self.assertGreater(self.model.updated_at, first_update)

    def test_to_dict(self):
        """Test of the dictionary representation of the attribute of the class"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['updated_at'], self.model.updated_at)
        self.assertEqual(model_dict['created_at'], self.model.created_at)



if __name__ == "__main__":
    unittest.main()