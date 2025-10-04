#!/usr/bin/python3
<<<<<<< HEAD
"""This is the user class"""
=======
"""
AirBnB Clone Project - User Model
Represents user accounts
"""
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(
        String(128),
        nullable=False)
    password = Column(
        String(128),
        nullable=False)
    first_name = Column(
        String(128),
        nullable=True)
    last_name = Column(
        String(128),
        nullable=True)
    places = relationship(
        "Place",
        backref="user",
        cascade="all, delete-orphan")
    reviews = relationship(
        "Review",
        backref="user",
        cascade="all, delete-orphan")
=======
    """
    User model for account management
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
