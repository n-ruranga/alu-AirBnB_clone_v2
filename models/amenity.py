#!/usr/bin/python3
<<<<<<< HEAD
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(
        String(128),
        nullable=False)
    place_amenities = relationship(
        "Place",
        secondary=place_amenity)
=======
"""
AirBnB Clone Project - Amenity Model
Represents property amenities
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity model for property features
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity',
                                   viewonly=True)
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
