"""The module that contain features that are common to other classes"""
# Importing required modules
import uuid
from datetime import datetime

class BaseModel:
    """The is the base class that other classes inherits from"""
    def __init__(self, id = None, created_at = None, updated_at = None):
        """Instantiating the BaseModel class
        
        Args:
            id: The unique value that identifies the object created
            created_at: A datetime object that tells the time of creation
            updated_at: A datetime object that tells the time of updating
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """The string method to print out the object in a user readable manner
        
        Return:
            A readable format of the object
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates with the new time when the function is called"""

        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
    

    