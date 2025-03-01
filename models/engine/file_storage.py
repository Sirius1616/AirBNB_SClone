import json
import os
from models.base_model import BaseModel





"""The module for making the data to persistent within the application"""
class FileStorage:
    """The class for serializing the objects into a persistent manner
    
    Attr:
        __file_path: path to the json file
        __objects: to store the class name object, it will be initially empty
    Methods:
        all: Returns the dictionary objects
        new: sets in __objects the obj with key <obj class name>.id
        reload: deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
    """

    __file_path = 'file.json'
    __objects = {}
    __classes = {'BaseModel' : BaseModel}
    

    def all(self):

        """The will return the dictionary of objects of the class created
        
        Returns:
            dict: Objects of the class
        """

        return FileStorage.__objects

    def new(self, obj):
        """Will set in the dictionary __objects the value for object
        
        Args:
            obj: the object to be ser in the dictionary of objects

        
        """

        classname = obj.__class__.__name__
        obj_id = obj.id
        key = str(classname) + '.' + str(obj_id)

        FileStorage.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as myfile:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, myfile)



    def reload(self):
        """Deserializes the JSON file back into objects (only if the file exists)."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        
        # Convert JSON back to objects
        FileStorage.__objects = {
            key: FileStorage.__classes[value["__class__"]](**value)
            for key, value in obj_dict.items()
        }

        

    
            
