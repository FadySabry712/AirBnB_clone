#!/usr/bin/python3
"""Defines Class FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Storage engine represntaion abstracted.
    Attributes:
        __file_path (str): The name of the file to save the objects.
        __objects (dict): A dict of the instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dict __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set up __objects obj with <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializess __objects to JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
