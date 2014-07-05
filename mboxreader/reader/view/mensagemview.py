#coding:latin
import glob
import mailbox

from reader import entityfactory, controllerfactory
from reader.view import projetoview
from util import conversordata

mensagemcontroller = controllerfactory.get('mensagem')
pessoacontroller = controllerfactory.get('pessoa')
projetocontroller = controllerfactory.get('projeto')
mensagem = entityfactory.get('mensagem')
pessoa = entityfactory.get('pessoa')
projeto = entityfactory.get('projeto')

def main():
    seleciona_projeto()

def seleciona_projeto():
    print('Projetos:')
    projetoview.listar()
    pId = int(input('Id do projeto:'))
    projeto = projetocontroller.get(id = pId)
    menu(projeto)

def menu(projeto):
    opcao = ''
    while opcao.lower() != 'q':
        print('\t\t', projeto.nome)
        opcao = input('Opcao:')
        if opcao == '1':
            carregar_mensagens(projeto)
        else:
            print('opcao inv�lida.')

def carregar_mensagens(projeto):
    for file in glob.glob(projeto.url + "/*.mbox"):
        file.replace('\\', '/')
        carrega_mensagems_arquivo(file, projeto)
    mensagemcontroller.atribui_pai_projeto(projeto)

def retorna_email(s):
    sl = s.split(' ')
    return sl[-1][1:-1]

def retorna_nome(s):
    sl= s.split("\"")
    return sl[0][1:-1]

def carrega_pessoa(msg):
    email = retorna_email(msg['from'])
    data_mensagem = conversordata.gera_data(msg['date'])
    p = pessoacontroller.get(email)
    if p== None:
        p = pessoa.Pessoa(email)
        p.dataEntrada = data_mensagem
        p.nome = retorna_nome(msg['from'])
    p.dataUltimoEMail = data_mensagem
    return p

def carrega_mensagem(msg, pessoa, projeto):
    m = mensagem.Mensagem(msg['from'], pessoa, projeto, to = msg['to'])
    m.date = msg['date']
    m.subject = msg['subject']
    m.in_reply_to = msg['in-reply-to']
    m.message_id = msg['message-id']
    m.references = msg['references']
    return m

def carrega_mensagems_arquivo(file, projeto):
    print('carregando: ', file)
    mensagens_carregadas=0
    mbox = mailbox.mbox(file)
    for msg in mbox:
        pessoa = carrega_pessoa(msg)
        mensagem = carrega_mensagem(msg, pessoa, projeto)
        mensagens_carregadas+=1
    print(str(mensagens_carregadas))
