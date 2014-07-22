#coding:latin

import sys
sys.path.append('.')
from reader import entityfactory, modelfactory, controllerfactory
from reader.view import projetoview, mensagemview
from util import database

pessoa = entityfactory.get('pessoa')
projeto = entityfactory.get('projeto')
mensagem = entityfactory.get('mensagem')
mensagemcontroller = controllerfactory.get('mensagem')
pessoacontroller = controllerfactory.get('pessoa')
projetocontroller = controllerfactory.get('projeto')

def main():
    database.criar()
    opcao = ''
    while opcao != 'q':
        opcao = input("Qual sua opção?").lower()
        if (opcao == '1'):
            projetoview.main()
        elif opcao == '2':
            mensagemview.main()



main()
