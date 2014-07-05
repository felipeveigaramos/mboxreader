#encoding:latin
from reader.dao import dao

def get(d):
    '''str->dao
    Retorna um dao.
    >>> get('dao')
    dao
    '''
    if d == 'dao':
        return dao
    return None
