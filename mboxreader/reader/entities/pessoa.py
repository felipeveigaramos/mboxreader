'''
Created on 30/03/2014

@author: FelipeVR
'''
from util.database import SingletonBase
from sqlalchemy import Column, Integer, String, DateTime

class Pessoa(SingletonBase()):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    dataEntrada = Column(DateTime(), nullable=False)
    dataUltimoEmail = Column(DateTime(), nullable=False)
    def __init__(self, email):
        self.email = email
