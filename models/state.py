#!/usr/bin/python3
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
                    if obj.state_id == self.id]
