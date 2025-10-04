#!/usr/bin/python3
<<<<<<< HEAD
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
=======
"""
AirBnB Clone Project - City Model
Represents cities within states
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False)
        state_id = Column(
            String(60),
            ForeignKey('states.id'),
            nullable=False)
        places = relationship(
            "Place",
            backref="cities",
            cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
=======
    """
    City model for urban areas
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='all, delete')
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
