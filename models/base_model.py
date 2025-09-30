#!/usr/bin/python3
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
Base = declarative_base()


class BaseModel:
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
