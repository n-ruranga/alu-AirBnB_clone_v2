#!/usr/bin/python3
<<<<<<< HEAD
"""This is the base model class for AirBnB"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

=======
"""
AirBnB Clone Project - Base Model
Core functionality for all model classes
"""
import uuid
import datetime
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


# SQLAlchemy declarative base (BaseModel does not inherit from Base)
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
Base = declarative_base()


class BaseModel:
<<<<<<< HEAD
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        my_dict = dict(self.__dict__)
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, my_dict)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        models.storage.delete(self)
=======
    """
    Base class providing common functionality for all model classes
    """

    # Common columns for mapped subclasses
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize instance with provided arguments or defaults"""
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                try:
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                except AttributeError:
                    pass
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()

    def save(self):
        """Update timestamp and persist to storage"""
        self.updated_at = datetime.datetime.utcnow()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance to dictionary representation"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        # Remove SQLAlchemy internal state if present
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """Delete current instance from storage"""
        from models import storage
        storage.delete(self)

    def __str__(self):
        """String representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                     self.__dict__)
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
