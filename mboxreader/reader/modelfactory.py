#coding:latin
'''
@aucthor Felipevr
'''
from reader.model import mensagemmodel, pessoamodel, projetomodel

def get(e):
    '''str->entity
    '''
    if e == 'mensagem':
        return mensagemmodel
    elif e == 'pessoa':
        return pessoamodel
    elif e == 'projeto':
        return projetomodel
