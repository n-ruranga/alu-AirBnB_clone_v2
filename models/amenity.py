#!/usr/bin/python3
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
