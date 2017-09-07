#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """State class handles all application states"""
    if storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ''

        @property
        def cities(self):
            """ returns list of City objects linked to current State """
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
