#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

#if getenv('HBNB_TYPE_STORAGE') == 'db':
    #Base = declarative_base()
#else:
    #Base = object

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if (kwargs.get('created_at') and type(self.created_at) is str):
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],'%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            if (kwargs.get('updated_at') and type(self.updated_at) is str):
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],'%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()
            if kwargs.get(id) == None:
                self.id = str(uuid.uuid4())

            del kwargs['__class__']
            self.__dict__.update(kwargs)


    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    #def delete(self):
        #""" Delete instance """
        #from models import storage
        #storage.delete(self)
    
    def delete(self):
        """Deletes the current instance from storage"""
        from models import storage
        storage.delete(self)


    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self) #Move storage.new(self)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # Remove _sa_instance_state key if it exists
        dictionary.pop('_sa_instance_state', None)

        return dictionary
