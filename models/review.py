#!/usr/bin/python3
<<<<<<< HEAD
"""This is the review class"""
=======
"""
AirBnB Clone Project - Review Model
Represents user reviews
"""
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(
        String(1024),
        nullable=False)
    place_id = Column(
        String(60),
        ForeignKey("places.id"),
        nullable=False)
    user_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False)
=======
    """
    Review model for user feedback
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
