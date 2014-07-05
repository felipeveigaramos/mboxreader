'''
Created on 31/03/2014

@author: FelipeVR
'''

class Projeto(object):
    #__storm_table__ = "projeto"
    def __init__(self, nome, url = ''):
        self.nome = nome
        #url=Unicode()
        self.url = url
        #id = Int(primary=True)
        self.id = 0

    def toString(self):
        return str(self.id) + ' ' + self.nome + ' ' + self.url
