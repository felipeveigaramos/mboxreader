# coding: latin
'''
Created on 03/03/2014

@author: FelipeVR
'''
import datetime
import mailbox

from reader.conversordata import gera_data




class Novato:
    def __init__(self, email, mensagem):
        self.email = email
        self.mensagem = mensagem
        self.tempo_resposta = datetime.timedelta(hours=-1)

    def get_tempo_resposta(self, u='h'):
        if u == 's':
            return self.tempo_resposta / datetime.timedelta(seconds=1)
        elif u == 'h':
            return self.tempo_resposta / datetime.timedelta(hours=1)
        elif u == 'd':
            return self.tempo_resposta / datetime.timedelta(days=1)
        else:
            return self.tempo_resposta

    def set_tempo_resposta(self, tempo_resposta):
        self.tempo_resposta = tempo_resposta

    def get_email(self):
        return self.email

    def get_mensagem(self):
        return self.mensagem


def retorna_email(s):
    sl = s.split(' ')
    return sl[-1][1:-1]

def gera_listas(mbox, date):
    novatos = []
    antigos = []
    for i in mbox.iterkeys():
        m = mbox.get(i)
        email = retorna_email(m['from'])
        if gera_data(m['date']) < date:
            if not email in antigos:
                antigos.append(email)
        else:
            if not email in antigos:
                if not email in novatos:
                    novatos.append(Novato(email, m))
    return (antigos, novatos)

def verifica_tempo_resposta(novatos):
    for novato in novatos:
        mensagem_novato = novato.get_mensagem()
        for mensagem in mailbox.mbox('201104.mbox'):
            if mensagem_novato['subject'] in mensagem['subject']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
            elif mensagem['references'] != None and mensagem_novato['Message-ID'] in mensagem['References']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
            elif mensagem_novato['message-id'] == mensagem['in-reply-to']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
    return novatos

def calcula_media_tempo_resposta(novatos):
    soma = 0
    for n in novatos:
        soma += n.get_tempo_resposta()
    return soma / len(novatos)

def media():
    date = datetime.datetime(2011, 4, 20)
    mbox = mailbox.mbox('mboxfiles/201104.mbox')
    print(mbox.keys())
    antigos, novatos = gera_listas(mbox, date)
    novatos = verifica_tempo_resposta(novatos)
 #   media = calcula_media_tempo_resposta(novatos)
#    print(media)
    print(len(novatos))


media()
