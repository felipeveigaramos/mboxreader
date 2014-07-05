#coding:latin
'''
@aucthor FelipeVR
'''
from util import conversordata
from reader import entityfactory, modelfactory
mensagem = entityfactory.get('mensagem')
mensagemmodel = modelfactory.get('mensagem')

def add(mensagem):
    mensagemmodel.add(mensagem)

def update(mensagem):
    return mensagemmodel.update(mensagem)

def get(projeto):
    return mensagemmodel.get(projeto)

def eh_pai(mensagem1, mensagem2):
    '''Mensagem, Mensagem -> bool
    Verifica se a mensagem 1 é a mensagem pai  da mensagem 2.
    '''
    if (mensagem2.message_id in mensagem1.references) or (mensagem2.message_id == mensagem1.in_reply_to):
        return True
    return False

def atribui_pai_mensagem(mensagens,mensagem):
    '''Mensagem[], mensagem ->
    A partir de uma lista de mensagens e uma mensagem,v erifica, nesta
lista, qual a mensagem pai, se esta existir.
    '''
    for msg in mensagens:
        if mensagem.mensagemPai == None and eh_pai(msg, mensagem):
            mensagem.mensagemPai = msg
            break

def atribui_pai_projeto(projeto):
    mensagens = get(projeto)
    for mensagem in mensagens:
        atribui_pai_mensagem(mensagens, mensagem)
