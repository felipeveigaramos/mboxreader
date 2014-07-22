'''
Created on 31/03/2014

@author: FelipeVR
'''
from util.database import SingletonBase
from sqlalchemy import Column, Integer, String


class Projeto(SingletonBase()):
    __tablename__ = 'projeto'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    url = Column(String(255), nullable = False)
    def __init__(self, nome, url = ''):
        self.nome = nome
        self.url = url

    def toString(self):
        return str(self.id) + ' ' + self.nome + ' ' + self.url
