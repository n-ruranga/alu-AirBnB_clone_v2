#!/usr/bin/python3
<<<<<<< HEAD
"""create a unique FileStorage instance for your application"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
=======
"""
Models package initialization
Sets up storage instance and loads existing data
"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
<<<<<<< HEAD
    storage.reload()
=======
    storage.reload()
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
