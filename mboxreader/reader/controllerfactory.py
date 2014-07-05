#coding:latin
'''
@aucthor Felipevr
'''
from reader.controller import mensagemcontroller, pessoacontroller, projetocontroller

def get(e):
    '''str->entity
    '''
    if e == 'mensagem':
        return mensagemcontroller
    elif e == 'pessoa':
        return pessoacontroller
    elif e == 'projeto':
        return projetocontroller
