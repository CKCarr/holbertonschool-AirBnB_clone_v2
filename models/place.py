#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Table, Column, ForeignKey, String, Integer, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os
Integer, String, Float, ForeignKey

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id',
                             String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity",
                                 secondary="place_amenity", viewonly=False,
                                 overlaps="place_amenities")
    else:
        @property
        def reviews(self):
            """ method gets a review list for linked reviews"""
            from models import storage
            from models.review import Review
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """ method gets and sets linked amenities """
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = storage.all(Amenity).values()
            for amenity in all_amenities:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """ Setter attribute amenities """
            from models.amenity import Amenity
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
