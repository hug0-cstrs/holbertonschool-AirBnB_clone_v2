#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
""" `getenv` to determine in which storage type we are
by scanning the HBNB_TYPE_STORAGE"""


class State(BaseModel, Base):
    """
    State class
    Establish a relationship with the class City
    """
    __tablename__ = 'states'
    """ db ==>  means let's go for SQLAlchemy logic"""
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter - returns the list of City instances
            with state_id == State.id
            FileStorage relationship between State and City
            """
            l_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    l_cities.append(city)
            return l_cities
