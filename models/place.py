"""Model for Place class"""
from models.base_model import BaseModel
from models.city import City
from models.user import User



class Place(BaseModel):
  """Model class for Place that inherits from the Basemodel class"""

  city_id = ""
  user_id = ""
  name = ""
  description = ""
  number_rooms = 0
  number_bathrooms = 0
  max_guest = 0
  price_by_night = 0
  latitude = 0.0
  longitude = 0.0
  amenity_ids = []
  
  def __init__(self, *args, **kwargs):
    """Instantiation of the model to inherite the attributes of the BaseModel"""
    super().__init__(*args, **kwargs)
    




