'''
@Aucthor felipevr
'''
from reader import daofactory, entityfactory
dao = daofactory.get('dao')
pessoa = entityfactory.get('pessoa')


def add(pessoa):
    '''str->
    Adiciona uma pessoa no banco de dados.
    '''
    dao.add(pessoa)

def get(email):
    return dao.get_pessoa(email)

def update(pessoa):
    dao.update(pessoa)

def get_novatos():
    return dao.get_novatos()
