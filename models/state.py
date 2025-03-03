"""Model for Place class"""
from models.base_model import BaseModel



class State(BaseModel):
  """Model class for Place that inherits from the Basemodel class"""

  name = ""

  def __init__(self, *args, **kwargs):
    """Instantiation of the model to inherite the attributes of the BaseModel"""
    super().__init__(*args, **kwargs)