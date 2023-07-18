#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenities class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary='place_amenity',
                                       overlaps="amenities")
    else:
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            @property
            def place_amenities(self):
                """ Getter attribute that returns the list of Place instances """
                from models import storage
                from models.place import Place
                place_amenities_list = []
                for place in storage.all(Place).values():
                    if place.amenity_ids == self.id:
                        place_amenities_list.append(place)
                return place_amenities_list
