#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls or value.__class__.__name__ == cls:
                    dict[key] = value
            return dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key in self.__objects:
            temp[key] = self.__objects[key].to_dict(True)
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """deletes obj from __objects"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()

        if obj is None:
            return

    def get(self, cls, id):
        """get one object"""
        if type(cls) == str:
            cls = self.__classes.get(cls)
        if cls is None:
            return None
        for item in self.__objects.values():
            if item.__class__ == cls and item.id == id:
                return item

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                val = json.load(f).values()
                for key in val:
                    name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(name)(**key))
        except FileNotFoundError:
            pass

    def close(self):
        """ reloads for deserializations of JSON file"""
        self.reload()
