'''
Created on 31/03/2014

@author: FelipeVR
'''
from reader.entities.pessoa import *
from reader.entities.projeto import *
from util.database import SingletonBase
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, backref

class Mensagem(SingletonBase()):
    __tablename__ = 'mensagem'
    id = Column(Integer, primary_key=True)
    message_from = Column(String(255), nullable=False)
    to = Column(String(255), nullable=False)
    subject = Column(String(255))
    date = Column(DateTime(), nullable=False)
    message_id = Column(String(255))
    in_reply_to = Column(String(255))
    references = Column(Text())
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa')
    projeto_id = Column(Integer, ForeignKey('projeto.id'))
    projeto= relationship('Projeto')
    mensagemPai_id = Column(Integer, ForeignKey('mensagem.id'))
    mensagemPai = relationship('Mensagem')


    def __init__(self, mFrom, pessoa, projeto, to = ''):
        self.message_from = mFrom
        self.to = to
        self.pessoa = pessoa
        self.projeto = projeto
