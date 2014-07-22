#coding:latin
'''
Arquivo com as operações no banco e seus objetos que devem se manter durante toda a aplicação.
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SingletonEngine():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = create_engine('mysql+mysqlconnector://root:root@localhost/mboxreader')
        return cls._instance

class SingletonBase():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = declarative_base()
        return cls._instance

class SingletonSession():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            Session = sessionmaker(bind=SingletonEngine())
            cls._instance = Session()
        return cls._instance




def criar():
    SingletonBase().metadata.create_all(SingletonEngine())
