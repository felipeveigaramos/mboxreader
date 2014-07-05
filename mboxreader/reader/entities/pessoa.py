'''
Created on 30/03/2014

@author: FelipeVR
'''
from datetime import datetime


class Pessoa(object):
    #__storm_table__ = "pessoa"
    def __init__(self, email, novato = False):
        #email = Unicode()
        self.email = email
        #novato = Bool()
        self.novato = novato
        self.id = 0
        #id = Int(primary=True)
        #nome = Unicode()
        self.nome = ''
        #dataEntrada = DateTime(1900, 1, 1)
        self.dataEntrada = datetime(1900, 1, 1)
        #dataUltimoEmail = DateTime()
        self.dataUltimoEmail = datetime(1900, 1, 1)
