"""Model for City class"""
from models.base_model import BaseModel
from models.state import State



class City(BaseModel):
  """Model class for city that inherits from the Basemodel class"""

  state_id = ""
  name = ""
  
  def __init__(self, *args, **kwargs):
    """Instantiation of the model to inherite the attributes of the BaseModel"""
    super().__init__(*args, **kwargs)
    