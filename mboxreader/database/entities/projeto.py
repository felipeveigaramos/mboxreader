'''
Created on 31/03/2014

@author: FelipeVR
'''
from storm.properties import Int, Unicode


class Projeto(object):
    __storm_table__ = "projeto"
    id = Int(primary=True)
    url=Unicode()
    