'''
Created on 01/04/2014

@author: FelipeVR
'''
from reader.database import fakedb

def add(entidade):
    fakedb.add(entidade)

def update(entidade):
    fakedb.update(entidade)

def get_mensagens(projeto):
    return fakedb.get_mensagens(projeto)

def get_pessoa(email):
    return fakedb.get_pessoa(email)

def get_projeto(id = -1, nome = ''):
    return fakedb.get_projeto(id = id, nome = nome)

def get_novatos():
    return fakedb.get_novatos()
