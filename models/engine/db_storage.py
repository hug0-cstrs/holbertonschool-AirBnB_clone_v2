#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
import os
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""DbStorage but why idk"""


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # Récupérer les informations de connexion de l'environnement
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        # Créer le moteur
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host} \
            {db}', pool_pre_ping=True
            )
        __session = Session(self.__engine)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        # all methode
        obj_dict = {}
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = type(obj).__name__ + "." + str(obj.id)
                    obj_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = type(obj).__name__ + "." + str(obj.id)
                obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        self.__session.remove()
