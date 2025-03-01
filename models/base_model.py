"""The module that contain features that are common to other classes"""
# Importing required modules
import uuid
from datetime import datetime
import models



strformat = '%Y-%m-%dT%H:%M:%S.%f'

class BaseModel:
    """The is the base class that other classes inherits from"""
    def __init__(self, *args, **kwargs):
        """Instantiating the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if hasattr(self, 'created_at') and isinstance(self.created_at, str):
                self.created_at = datetime.fromisoformat(self.created_at)
            if hasattr(self, 'updated_at') and isinstance(self.updated_at, str):
                self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """The string method to print out the object in a user readable manner
        
        Return:
            A readable format of the object
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates with the new time when the function is called"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary representation of the class object"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()  # Convert to string
        new_dict['updated_at'] = self.updated_at.isoformat()  # Convert to string
        
        return new_dict
    

    