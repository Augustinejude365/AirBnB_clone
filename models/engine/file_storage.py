#!usr/bin/python3

"""
Defines the file storage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A line of code that Serializes an instance to JSON and
    deserializes back to instance object
    """
    # Stores all objects by <class name>.id
    __objects = {}
    # Path to the JSON file.
    __file_path = "file.json"

    def all(self, cls=None):
        """This returns a dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """
        This line of codes sets in __ojbects the obj with key <obj
        class name >.id
        """
        if obj is not None:
            # Concatenate class object name with id.
            key = obj.__class__.__name__+"."+obj.id
            # update the __object dictionary with the new key and
            # object as valu.
            self.__objects[key] = obj

    def save(self):
        """
        This Serializes __objects to the JSON File(path:__file_path)
        """
        j_objects = {}
        # For the python data to be serialized, the data stored
        # inside the __objec variable as objects must be converted
        # to a dictionary so that pytho for json will understand
        # using to_dict method of the basemodel class
        # The result of this will be a key with a unique dictionary
        # as the value.
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
            # Convert the dictionary into json and save in __filepath.
            with open(self.__file_path, 'w') as f:
                json.dump(j_objects, f)

    def reload(self):
        """
        This deserializes the JSON file to __objs(only if the JSON
        file(__file_path) exists; otherwise does nothing, no
        exception should be raised if the file does not exist.
        """
        try:
            with open(self.__file_path, 'r', encoding="utf8") as f:
                # The load method deserializes a json string into
                # a python dictionary
                obj_dict = json.load(f)
                for obj_item in obj_dict.values():
                    # Extract the class from which to instantiate an object.
                    # Note that the values were loaded, and not the keys.
                    class_name = obj_item["__class__"]
                    # The attribute __class__\ should not be passed
                    # as part of the arguments init since we are
                    # creating object instances function of the class
                    # (identified by class_name) all the other
                    # arguments are valid.

    del obj_item["__class__"]
    # We used the previously defined new function to create a new __obj.
    # Note that the double asterics expands the dictionary to allow
    # every key value pair from object_item dict to be passed to the
    # __init__() method of the class identified by class_name
    self.new(eval(class_name)(**obj_item))
    except FileNotFoundError:
        pass
