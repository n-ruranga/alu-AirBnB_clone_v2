#!/usr/bin/python3
<<<<<<< HEAD
"""This is the file storage class for AirBnB"""
from models.base_model import BaseModel, Base
=======
"""
AirBnB Clone Project - DB Storage
SQLAlchemy-based storage engine
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class stores data to the MySQL database
    Attributes:
        __engine: None
        __session: None
    """
    __engine = None
    __session = None
    all_classes = {"State", "City", "User", "Amenity", "Place", "Review"}

    def __init__(self):
        """create the engine and links it to the MySQL database and user"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary of instances/objects
        Return:
            returns a dictionary like FileStorage (__objects)
        """
        if cls:
            try:
                return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                        for obj in self.__session.query(eval(cls)).all()
                        if eval(cls).__name__ == type(obj).__name__}
            except:
                return {}
        else:
            obj_list = []
            for cls_name in self.all_classes:
                for obj in self.__session.query(eval(cls_name)).all():
                    obj_list.append(obj)
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for obj in obj_list}

    def new(self, obj):
        """add the object to the current database session
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def reload(self):
        """create all tables in the database
        and create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scoped_Session = scoped_session(Session)
        self.__session = Scoped_Session()

    def delete(self, obj=None):
        """delete obj from the current database session
        """
        if obj:
            self.__session.delete(obj)
        self.save()

#    Note: leave this here, might use later?
#    Not sure why we are NOT being asked to close the sessions
#    In Project 0x0F, I always closed sessions prior to terminating
#    That is a question we should ask
#
    def close(self):
        """close the current database session
        """
        self.__session.close()
=======


class DBStorage:
    """Database storage engine using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine based on environment variables"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current session for all objects of class cls or all classes.

        Returns a dict of key -> obj, where key is <class-name>.<id>.
        """
        result = {}
        classes = [User, State, City, Amenity, Place, Review]
        target_classes = classes
        if cls is not None:
            if isinstance(cls, str):
                target_classes = [c for c in classes if c.__name__ == cls]
            else:
                target_classes = [cls]
        for c in target_classes:
            for obj in self.__session.query(c).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """Add object to current database session"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session if provided"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize the session"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)()


>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
