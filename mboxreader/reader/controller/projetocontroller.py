'''
@aucthor Felipevr
'''
from reader import entityfactory, modelfactory
projeto = entityfactory.get('projeto')
projetomodel = modelfactory.get('projeto')

def add(projeto):
    projetomodel.add(projeto)

def update(projeto):
    projetomodel.update(projeto)

def get(id = -1, nome = ''):
    return projetomodel.get(id = id, nome = nome)
