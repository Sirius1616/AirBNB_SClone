"""The module for making the data to persistent within the application"""
class Filestoage:
    """The class for serializing the objects into a persistent manner
    
    Attr:
        __file_path: path to the json file
        __objects: to store the class name object, it will be initially empty
    Methods:
        all: Returns the dictionary objects
        new: sets in __objects the obj with key <obj class name>.id
        
    """