#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


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

    user = relationship("models.user.User", backref="places")
    city = relationship("models.city.City", backref="places")
    amenities = relationship(
        "models.amenity.Amenity", secondary=place_amenity, backref="places")

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
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

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        @property
        def amenities(self):
            """ method gets and sets linked amenities """
            from models import storage
            from models.amenity import Amenity

            amenity_list = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if self.id == amenity.place_id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """ Setter attribute amenities """
            from models.amenity import Amenity

            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
