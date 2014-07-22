'''
Created on 01/04/2014

@author: FelipeVR
'''
from reader.database import fakedb
from util.database import *
from reader import entityfactory

mensagem = entityfactory.get('mensagem')
pessoa = entityfactory.get('pessoa')
projeto = entityfactory.get('projeto')

def add(entidade):
    session = SingletonSession()
    session.add(entidade)
    session.commit()

def update(entidade):
    session = SingletonSession()
    session.commit()


def get_mensagens(p):
    session = SingletonSession()
    query = session.query(mensagem.Mensagem)
    return query.filter(mensagem.Mensagem.projeto == p).order_by(mensagem.Mensagem.date).all()


def get_pessoa(email):
    session = SingletonSession()
    query = session.query(pessoa.Pessoa)
    return query.filter(pessoa.Pessoa.email == email).first()

def get_projeto(id = -1, nome = ''):
    session = SingletonSession()
    query = session.query(projeto.Projeto)
    if (id != -1):
        return query.filter(projeto.Projeto.id == id).first()
    elif nome != '':
        query.filter(projeto.Projeto.nome.like('%' + nome + '%')).order_by(projeto.Projeto.id)
    return query.all()




def get_novatos():
    return fakedb.get_novatos()
