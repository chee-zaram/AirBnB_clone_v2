#!/usr/bin/python3

"""This module defines a ``DBStorage`` class
for the MySQL storage option for the Airbnb clone
"""
from sqlalchemy import create_engine
from models import Base, BaseModel, City, State
from models import Place, Amenity, Review, User
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBStorage():
    """Defines the MySQL database storage class"""

    __engine = None
    __session = None
    __valid_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
        }

    def __init__(self):
        """Initializes a ``DBStorage`` class instance

        Atributes:
        """
        dev_environ = getenv("HBNB_ENV", "Please set environment")
        user = getenv("HBNB_MYSQL_USER", "Please set user")
        password = getenv("HBNB_MYSQL_PWD", "Please set password")
        host = getenv("HBNB_MYSQL_HOST", "Please set host")
        database = getenv("HBNB_MYSQL_DB", "Please set database")
        port = 3306

        url = f"mysql+mysqldb://{user}:{password}@{host}:{port}/{database}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if dev_environ == "test":
            Base.metdata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instances of all the classes
        in the database, or of a class, if specified"""

        db_storage = []

        if cls and cls in DBStorage.__valid_classes:
            db_storage = self.__session.query(cls).all()
        else:
            for key in DBStorage.__valid_classes:
                db_storage.extend(self.__session
                                  .query(DBStorage.__valid_classes[key]).all())
        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in db_storage}

    def new(self, obj):
        """Adds an object to the current database session """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the tables from the MySQL database"""
        Base.metadata.create_all(self.__engine, checkfirst=True)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()