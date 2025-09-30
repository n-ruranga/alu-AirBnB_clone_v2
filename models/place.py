#!/usr/bin/python3
"""
AirBnB Clone Project - Place Model
Represents rental properties
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """
    Place model for rental properties
    Inherits all functionality from BaseModel
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    from models.amenity import Amenity  # circular import guard for typing

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.base_model import Base
        place_amenity = Table(
            'place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
                   primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                   primary_key=True, nullable=False)
        )
        reviews = relationship('Review', backref='place', cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            return [obj for obj in storage.all(Review).values()
                    if obj.place_id == self.id]

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            return [obj for obj in storage.all(Amenity).values()
                    if obj.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if isinstance(value, Amenity):
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
