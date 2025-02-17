#!/usr/bin/python3
""" City Module for HBNB project """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = {
    'City': City,
    'User': User,
    'Review': Review,
    'State': State,
    'Place': Place,
    'Amenity': Amenity
}


class DBStorage:
    """ class DBStorage that will interact with the MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ the init that give HBNB envelopes?"""
        user = os.getenv('HBNB_MYSQL_USER')
        pw = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        dir = "mysql+mysqldb://{}:{}@{}/{}".format(user, pw, host, db)

        self.__engine = create_engine(dir, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects of a class or all classes"""
        classes = [City, State, User, Place, Amenity, Review]
        class_dict = {}

        if cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                class_dict[key] = obj
        elif cls is None:
            for cls in classes:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    class_dict[key] = obj

        return class_dict

    def new(self, obj):
        """ method new adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ method save commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ method delete deletes from the current database session
        obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ method reload creates a session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the storage"""
        Session.close_all()
