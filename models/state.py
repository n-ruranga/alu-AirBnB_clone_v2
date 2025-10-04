#!/usr/bin/python3
<<<<<<< HEAD
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter - returns the list of City instances"""
            return [obj for (key, obj) in
                    models.storage.all(models.City).items()
=======
"""
AirBnB Clone Project - State Model
Represents geographical states
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """
    State model for geographical regions
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            # Return list of City instances with matching state_id
            return [obj for obj in storage.all(City).values()
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
                    if obj.state_id == self.id]
