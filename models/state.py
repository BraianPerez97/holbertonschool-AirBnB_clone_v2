#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import City
import models
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


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
