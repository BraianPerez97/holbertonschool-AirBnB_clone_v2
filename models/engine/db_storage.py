#!/usr/bin/python3

""" This module defines a class that manages database storage fro hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


username = os.getenv('HBNB_MYSQL_USER')
passwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """
    This class manages storage of hbnb models to SQL
    """
    __engine = None
    __session = None
    __classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                 "Place": Place, "Review": Review, "State": State, "User": User}

    def __init__(self):
        """ Constructor for the class DBStorage """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(username, passwd, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns objects in dictionary format """
        dict = {}
        if cls in self.__classes:
            results = self.__session.query(cls).all()
            for result in results:
                key = "{}.{}".format(result.__class__.__name__, result.id)
                dict[key] = result
        return dict

    def new(self, obj):
        """ Adds new object to current db session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from current db session if not none """
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """ Retrieves class obj"""
        if type(cls) == str:
            cls = self.__classes.get(cls)
        if cls is None:
            return None
        return self.__session.query(cls).filter(cls.id == id).first()

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if type(cls) is str:
            cls = self.__classes.get(cls)
        if cls is None:
            return len(self.all())
        return len(self.all(cls))

    def reload(self):
        """ Creates current db session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session

    def close(self):
        """ Close Session """
        self.__session.remove()
