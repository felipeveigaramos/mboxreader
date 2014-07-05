'''
Created on 02/04/2014

@author: FelipeVR
'''

projetos = []
ULTIMA_ID_PROJETOS = 0
pessoas = []
ULTIMA_ID_PESSOAS = 0
mensagens = []
ULTIMA_ID_MENSAGENS = 0

def add(entidade):
    #gambitec:alterando variaveis globais na função
    global ULTIMA_ID_PESSOAS
    global ULTIMA_ID_PROJETOS
    global ULTIMA_ID_MENSAGENS
    module = entidade.__module__
    if module == "reader.entities.mensagem" and not (entidade in mensagens):
        mensagens.append(entidade)
        ULTIMA_ID_MENSAGENS +=1
        entidade.id = ULTIMA_ID_MENSAGENS
    elif module == 'reader.entities.pessoa' and not (entidade in pessoas):
        print(entidade.email)
        pessoas.append(entidade)
        ULTIMA_ID_PESSOAS+=1
        entidade.id = ULTIMA_ID_PESSOAS
    elif module == 'reader.entities.projeto' and not (entidade in projetos):
        projetos.append(entidade)
        ULTIMA_ID_PROJETOS += 1
        entidade.id = ULTIMA_ID_PROJETOS

def get_pessoa(email):
    for pessoa in pessoas:
        if (pessoa.email == email):
            return pessoa
    return None

def get_mensagens(projeto):
    mensagens_in_projeto = []
    for mensagem in mensagens:
        if mensagem.projeto == projeto:
            mensagens_in_projeto.append(mensagem)
    return mensagens_in_projeto

def get_projeto(id = -1, nome = ''):
    projetosr = []
    for projeto in projetos:
        if projeto.id == id or projeto.nome == nome:
            return projeto
        elif id == -1 and nome == '':
            projetosr.append(projeto)
    return projetosr

def update(entidade):
    if entidade.id == None or entidade.id <= 0:
        return False

    module = entidade.__module__
    if module == "mensagem":
        mensagens[entidade.id] = entidade
    elif module == 'pessoa' and not (entidade in pessoas):
        pessoas[entidade.id] = entidade
    elif module == 'projeto' and not (entidade in projetos):
        projetos[entidade.id] = entidade
    return True

def get_novatos():
    novatos = []
    for pessoa in pessoas:
        if pessoa.novato == True:
            novatos.append(pessoa)
    return novatos
