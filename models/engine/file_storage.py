#!/usr/bin/python3
"""File Storeage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retrieve __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add Object to __objects"""
        key_str = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key_str] = obj

    def remove(self, key_val):
        if FileStorage.__objects.get(key_val) is not None:
            del FileStorage.__objects[key_val]

    def save(self):
        """Save __objects to __file_path"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as objFile:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, objFile)

    def reload(self):
        """Load objects from __file_path"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8")\
                       as fileobj:
                temp = json.load(fileobj)
                for k, v in temp.items():
                    restoredObject = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = restoredObject
        except FileNotFoundError:
            pass