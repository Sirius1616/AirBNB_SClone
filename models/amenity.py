"""Model for Amenity class"""
from models.base_model import BaseModel



class Amenity(BaseModel):
  """Model class for amenity that inherits from the Basemodel class"""

  name = ""
  
  def __init__(self, *args, **kwargs):
    """Instantiation of the model to inherite the attributes of the BaseModel"""
    super().__init__(*args, **kwargs)
    
