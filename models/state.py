#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
from models import City
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from models import storage


class State(BaseModel, Base):
    """This is the class for State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    if models.storage_t == 'db':
        @property
        def cities(self):
            """Getter attribute that returns the list of City objects
            linked to the current State"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list  # !/usr/bin/python3


""" State Module for HBNB project """


class State(BaseModel, Base):
    """ State class """
    from models import storage
    if storage == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)

        # relationship
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """inits state"""
        super().__init__(*args, **kwargs)

    if models.storage != 'db':
        @property
        def cities(self):
            """getter that returns list of cities"""
            from models import storage
            city_list = []
            all_cities = storage.all(City)

            for city in all_cities.values():
                if self.id == city.state_id:
                    city_list.append(city)

            return city_list
