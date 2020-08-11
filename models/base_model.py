#!/usr/bin/python3
"""
Base class to models
"""

import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''
    if storage_type == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(
            DateTime, default=datetime.utcnow(), nullable=False)
        updated_at = Column(
            DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if len(kwargs) == 0:
            # if no dictionary of attributes is passed in
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            # assign a dictionary of attributes to instance

            # preserve existing created_at time
            if kwargs.get('created_at'):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()  # assign current time
            if kwargs.get('updated_at'):
                # preserve existing updated_at time
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.utcnow()

            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel class.
        '''
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        if 'updated_at' in cp_dct:
            cp_dct['updated_at'] = self.updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        if 'created_at' in cp_dct:
            cp_dct['created_at'] = self.created_at.strftime(
                "%Y-%m-%dT%H:%M:%S.%f")
        if '_sa_instance_state' in cp_dct:
            cp_dct.pop('_sa_instance_state', None)
        return (cp_dct)

    def delete(self):
        """From delete data"""
        models.storage.delete(self)
