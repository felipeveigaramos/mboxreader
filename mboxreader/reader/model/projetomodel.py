#encoding:latin
'''
@aucthor Felipevr
'''
from reader import daofactory,entityfactory
dao = daofactory.get('dao')
projeto = entityfactory.get('projeto')

def add(projeto):
    dao.add(projeto)

def get(id = -1, nome = ''):
    return dao.get_projeto(id = id, nome = nome)

def update(projeto):
    dao.update(projeto)
