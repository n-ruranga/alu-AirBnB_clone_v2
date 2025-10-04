#!/usr/bin/python3
<<<<<<< HEAD
"""This is the file storage class for AirBnB"""
=======
"""
AirBnB Clone Project - File Storage
JSON-based persistence layer for model objects
"""
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
<<<<<<< HEAD
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls:
            try:
                return {k: v for (k, v) in FileStorage.__objects.items()
                        if cls.__name__ == k.split('.')[0]}
            except:
                return {}
        else:
            return FileStorage.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
=======
    """
    Handles serialization and deserialization of objects to/from JSON
    """

    __file_path = 'file.json'
    __objects = {}
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def all(self, cls=None):
        """Return all stored objects, optionally filtered by class.

        Args:
            cls: Optional class or class name to filter results.

        Returns:
            dict mapping keys to objects. If cls is provided, only
            objects of that class are returned.
        """
        if cls is None:
            return FileStorage.__objects
        # Accept both class objects and class name strings
        cls_name = cls if isinstance(cls, str) else getattr(cls, "__name__", None)
        if cls_name is None:
            return FileStorage.__objects
        filtered = {}
        for key, obj in FileStorage.__objects.items():
            if key.split('.')[0] == cls_name:
                filtered[key] = obj
        return filtered

    def new(self, obj):
        """Add new object to storage with class.id key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize all objects to JSON file"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """Load objects from JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                f_contents = f.read()
                dict_obj_dicts = json.loads(f_contents)
            for key in dict_obj_dicts.keys():
                obj_dict = dict_obj_dicts[key]
                FileStorage.__objects[key] = FileStorage\
                           .className[key.split('.')[0]](**obj_dict)
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """delete obj from __objects if it’s inside
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]
        self.save()

    def close(self):
        """function that calls the reload() method for deserializing
        the JSON file to objects
        """
        self.reload()
=======
        """Delete obj from __objects if it exists.

        If obj is None, do nothing.
        """
        if obj is None:
            return
        key = '{}.{}'.format(obj.__class__.__name__, getattr(obj, 'id', None))
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
