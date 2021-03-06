#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """This is the class for State
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = 'cities'
    if storage_type == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place", cascade="delete", backref="cities")
    else:
        state_id = ""
        name = ""
