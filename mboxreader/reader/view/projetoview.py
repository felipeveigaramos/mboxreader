#coding:latin
from reader import entityfactory, controllerfactory

projeto = entityfactory.get('projeto')
projetoController = controllerfactory.get('projeto')

def listar():
    projetos = projetoController.get()
    for p in projetos:
        print(p.toString())

def add():
    nome = input('Nome do projeto:')
    url = input('url do projeto')
    p = projeto.Projeto(nome, url)
    projetoController.add(p)
    if p.id>0:
        print('adicionado')
    else:
        print('falha ao adicionar projeto')

def update():
    listar()
    id = int(input('Numero do projeto:'))
    p = projetoController.get(id = id)
    opcao = ''
    while opcao.lower() != 'q':
        print('n\tnome\nu\turl\nq\tsair')
        print(p.toString())
        opcao = input('opção?').lower()
        if opcao == 'q':
            ...
        elif opcao == 'n':
            nome = input('Nome:')
            p.nome = nome
            projetoController.update(p)
        elif opcao == 'u':
            url = input('url:')
            p.url= url
            projetoController.update(p)
        else:
            print('Opção inválida.')

def main():
    opcao = ''
    while opcao != 'q':
        print('Projeto - h ajuda.')
        opcao = input('Opção:').lower()
        if opcao == 'q':
            ...
        elif opcao == '1':
            listar()
        elif opcao == '2':
            add()
        elif opcao == '3':
            update()
        else:
            print('Opção inválida.')
