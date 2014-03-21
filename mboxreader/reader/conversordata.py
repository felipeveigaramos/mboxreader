# coding: latin
'''
Created on 25/02/2014
Converte datas de mbox, em texto, para formatos mais amigáveis. Atualmente, datetime.
@author: FelipeVR
'''
from datetime import datetime

def numero_mes(s):
    '''str->int
    Retorna o número correspondente para um dado mês, em inglês.
    >>> numero_mes('Jan')
    1
    >>> numero_mes('Dec')
    12
    >>> numero_mes('bat')
    0
    '''
    if s == 'Jan':
        return 1
    elif s == 'Feb':
        return 2
    elif s == 'Mar':
        return 3
    elif s == 'Apr':
        return 4
    elif s == 'May':
        return 5
    elif s == 'Jun':
        return 6
    elif s == 'Jul':
        return 7
    elif s == 'Ago':
        return 8
    elif s == 'Set':
        return 9
    elif s == 'Out':
        return 10
    elif s == 'Nov':
        return 11
    elif s == 'Dez':
        return 12
    return 0

def gera_data(data_string):
    '''string -> datetime
    Converte uma data em texto para timedate.
    
    '''
    data_string_list = data_string.split(' ')
    day = 1
    month = 1
    year = 1900
    horas_list = [0, 0, 0]
    
    if ((len(data_string) == 36 or len(data_string) == 37)
and len(data_string_list) == 7) or ((len(data_string) == 25 or len(data_string) == 26) and len(data_string_list) == 5) or ((len(data_string) == 30 or len(data_string) == 31) and len(data_string_list) == 6):
        extra = 0 #algumas datas possuem valor maior de dados e o primeiro deve ser ignorado
        if len(data_string_list) == 7 or len(data_string_list) == 6:
            extra = 1
        horas_list = data_string_list[3+extra].split(':')
        year = data_string_list[2+extra] 
        month = numero_mes(data_string_list[1+extra]) 
        day = data_string_list[0+extra]
        print(str(extra) + " " + str(data_string_list[0]) + " " + str(data_string_list[1]) + " " + str(data_string_list[2]))    
    elif ((len(data_string) == 24 or len(data_string) == 25) and len(data_string_list) == 5):
        horas_list = data_string_list[3].split(':')
        year = data_string_list[-1] 
        month = numero_mes(data_string_list[1]) 
        day = data_string_list[2]
        
    data = datetime(int(year), month, int(day), int(horas_list[0]), int(horas_list[1]), int(horas_list[2]))
    print(data_string + " " + str(data))
    return data