'''
Created on 30/03/2014

@author: FelipeVR
'''
from storm.locals import *

class Pessoa(object):   
    __storm_table__ = "pessoa"
    id = Int(primary=True)
    nome = Unicode()
    email = Unicode()
    dataEntrada = DateTime()
    dataUltimoEMail = DateTime()
    novato = Bool()
    
    
    