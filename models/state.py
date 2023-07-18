#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
# from models import storage
# from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """city getter"""
            from models import storage
            from models.city import City
            city_list = []
            all_cities = storage.all(City)
            for obj in all_cities.values():
                if self.id == obj.state_id:
                    city_list.append(obj)
            return city_list
