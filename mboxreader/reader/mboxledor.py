# coding: latin
'''
Created on 03/03/2014
    
@author: FelipeVR
'''
import datetime
from mailbox import mbox
import mailbox

from database import fakedb
from database.entities import *
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


def e_resposta(msg, mensagem):
    if (mensagem.subject in msg.subject) or (mensagem.message_id in msg.references) or (mensagem.message_id == msg.in_reply_to):
        return True
    return False


def atribui_pai(mensagem):
    for msg in fakedb.getbd():
        if e_resposta(msg, mensagem):
            mensagem.mensagemPai = msg


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
    
    atribui_pai(mensagem)
    
    return mensagem

def gera_lista(mbox, data):
    for msg in mbox:        
        data_mensagem = gera_data(msg['date'])
        pessoa = retorna_pessoa(msg, data, data_mensagem)
        mensagem = retorna_mensagem(msg, pessoa)
        fakedb.add(mensagem)
        print('%i' % len(fakedb.getbd()))


gera_lista(mailbox.mbox('mboxfiles/201104.mbox'), datetime.datetime(2011, 4, 20))        