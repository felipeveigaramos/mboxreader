'''
Created on 31/03/2014

@author: FelipeVR
'''
from storm.properties import Int, Unicode, DateTime


class Mensagem(object):
    __storm_table__ = "mensagem"
    id = Int(primary=True)
    message_from = Unicode() #Necess�rio j� que from � uma palavra reservada
    to = Unicode()
    subject = Unicode()
    date = DateTime()
    message_id = Unicode()
    in_reply_to = Unicode()
    references = Unicode()
#Olhe aqui Felipe o que eu comentei
#    mensagemPai = reference(mensagemPaiId, Mensagem.id)
#    pessoa = reference(pessoaId, Pessoa.id)
#    projeto = reference(projetoId, Projeto.id)
    
    
    
    
    
    
    
    
    
