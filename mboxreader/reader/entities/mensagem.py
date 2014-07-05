'''
Created on 31/03/2014

@author: FelipeVR
'''
from datetime import datetime
from reader.entities.pessoa import *
from reader.entities.projeto import *

class Mensagem(object):
    #__storm_table__ = "mensagem"
    def __init__(self, mFrom, pessoa, projeto, to = ''):
        #message_from = Unicode() #Necessario ja que from eh uma palavra reservada
        self.message_from = mFrom
        #to = Unicode()
        self.to = to
        #pessoa = reference(pessoaId, Pessoa.id)
        self.pessoa = pessoa
        #projeto = reference(projetoId, Projeto.id)
        self.projeto = projeto
        #id = Int(primary=True)
        self.id = 0
        #subject = Unicode()
        self.subject = ''
        #date = DateTime()
        self.date = datetime(1900, 1, 1)
        #message_id = Unicode()
        self.message_id = ''
        #in_reply_to = Unicode()
        self.in_reply_to = ''
        #references = Unicode()
        self.references = ''
        self.mensagemPai = None
