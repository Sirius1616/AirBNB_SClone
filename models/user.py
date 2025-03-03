"""A module for the class"""
from models.base_model import BaseModel

class User(BaseModel):
    """A User model that inherits all the methods from the BaseModel which is meant to create users for the model
    
    Methods

    """

    def __init__(self, *args, **kwargs):
        """Instantiation of the User class with the email, password, first_name, last_name
        
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    

    
