'''
@Aucthor felipevr
'''
from reader import entityfactory
from reader import modelfactory
pessoamodel = modelfactory.get('pessoa')
pessoa = entityfactory.get('pessoa')

def add(pessoa):
    '''str->
    Adiciona uma pessoa no banco de dados.
    '''
    pessoamodel.add(pessoa)

def get(email):
    return pessoamodel.get(email)

def update(pessoa):
    pessoamodel.update(pessoa)

def get_novatos():
    return pessoamodel.get_novatos()
