#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenities class"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places = relationship('Place', secondary='place_amenity',
                          backref='amenities')
    place_amenities = relationship('Place', secondary="place_amenity",
                                   overlaps="places")
