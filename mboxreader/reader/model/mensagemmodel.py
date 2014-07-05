'''
@aucthor felipevr
'''
from reader import entityfactory,daofactory
mensagem = entityfactory.get('mensagem')
dao = daofactory.get('dao')

def add(mensagem):
    dao.add(mensagem)

def update(mensagem):
    return dao.update(mensagem)

def get(projeto):
    return dao.get_mensagens(projeto)
