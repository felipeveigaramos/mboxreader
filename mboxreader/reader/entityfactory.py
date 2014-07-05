# coding: latin

from reader.entities import mensagem,pessoa,projeto

def get(e):
    '''str -> entity
    Com base no nome da entidade, retorna seur espectivo módulo.
    >>> get('pessoa')
    pessoa
    '''
    if e == 'mensagem':
        return mensagem
    elif e == 'pessoa':
        return pessoa
    elif e == 'projeto':
        return projeto
    return None
