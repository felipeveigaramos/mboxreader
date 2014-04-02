'''
Created on 02/04/2014

@author: FelipeVR
'''



lista = []
 
def add(mensagem):
    lista.append(mensagem)
    
def get_pessoa(email):
    for m in lista:
        if (m.pessoa.email == email):
            return m.pessoa
    return ... 

def getbd():
    return lista