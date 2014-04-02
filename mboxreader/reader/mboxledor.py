# coding: latin
'''
Created on 03/03/2014
    
@author: FelipeVR
'''
import datetime
from mailbox import mbox
import mailbox

from database import fakedb
from database.entities.mensagem import Mensagem
from database.entities.pessoa import Pessoa
from reader.conversordata import gera_data


def retorna_email(s):
    sl = s.split(' ')
    return sl[-1][1:-1]

def retorna_pessoa(mensagem, data, data_mensagem):
    email = retorna_email(mensagem['from'])
    pessoa = fakedb.get_pessoa(email)
    if pessoa == ...:
        pessoa = Pessoa()
        pessoa.email = email
        pessoa.dataEntrada = data_mensagem
        if data.before(data_mensagem):
            pessoa.novato = True
    pessoa.dataUltimoEMail = data_mensagem
    return pessoa        


def retorna_mensagem(msg, pessoa):
    mensagem = Mensagem()
    mensagem.message_from = msg['from']
    mensagem.date = msg['date']
    mensagem.subject = msg['subject']
    mensagem.to = msg['to']
    mensagem.in_reply_to = msg['in-reply-to']
    mensagem.message_id = msg['message-id']
    mensagem.references = msg['references']
    mensagem.pessoa = pessoa
    
    return mensagem

def gera_lista(mbox, data):
    for msg in mbox:        
        data_mensagem = gera_data(msg['date'])
        pessoa = retorna_pessoa(msg, data, data_mensagem)
        mensagem = retorna_mensagem(msg, pessoa)
        