#!/usr/bin/python3

import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBStorage():
    """ DataBase for hbnb """
    
    # Private class attrs engine and session set to none
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the class """
        # Create the engine
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns a dictionary"""
        objects = {}

        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for sub_cls in Base.__subclasses__():
                for obj in self.__session.query(sub_cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """ Adds new objects """
        self.__session.add(obj)

    def save(self):
        """Saves all changes made"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes objects """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables """
        Base.metadata.create_all(self.__engine)
        Mysession = sessionmaker(bind=self.__engine, expire_on_commit=False)

        Session = scoped_session(Mysession)
        self.__session = Session()

    def close(self):
        """ calls remove method on the private session attr """
        self.__session.remove()
