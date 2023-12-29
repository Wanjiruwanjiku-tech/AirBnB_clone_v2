#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship for DBStorage
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',cascade='all, delete')
    else:
        # Getter attribute for FileStorage

        @property
        def cities(self):
            """Getter attr for cities in FileStorage"""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            
            return city_list
