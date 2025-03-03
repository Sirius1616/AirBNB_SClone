"""A module for the class"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
  """Model class for Review that inherits from the Basemodel class"""

  place_id = ""
  user_id = ""
  text = ""

  def __init__(self, *args, **kwargs):
    """Instantiation of the model to inherite the attributes of the BaseModel"""
    super().__init__(*args, **kwargs)
    
