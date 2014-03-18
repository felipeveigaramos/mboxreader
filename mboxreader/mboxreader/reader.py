import datetime
import mailbox
#tentando de novo...
class Novato:
    def __init__(self, email, mensagem):
        self.email = email
        self.mensagem = mensagem
        self.tempo_resposta = datetime.timedelta(hours=-1)

    def get_tempo_resposta(self, u='h'):
        if u == 's':
            return self.tempo_resposta/datetime.timedelta(seconds=1)
        elif u == 'h':
            return self.tempo_resposta/datetime.timedelta(hours=1)
        elif u == 'd':
            return self.tempo_resposta/datetime.timedelta(days=1)
        else:
            return self.tempo_resposta

    def set_tempo_resposta(self, tempo_resposta):
        self.tempo_resposta = tempo_resposta

    def get_email(self):
        return self.email

    def get_mensagem(self):
        return self.mensagem

def numero_mes(s):
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

def gera_data(s):
    """str->datetime
    """
    date_string_list = s.split(' ')
    extra = 0 #Algumas datas iniciam com o nome da semana que deve ser ignorado.
    if len(date_string_list) > 5:
        extra += 1

    hour_string_list = date_string_list[3+extra].split(':')
    date = datetime.datetime(int(date_string_list[2+extra]),
numero_mes(date_string_list[1+extra]), int(date_string_list[0+extra]), int(hour_string_list[0]), int(hour_string_list[1]), int(hour_string_list[2]))
    return date

def retorna_email(s):
    sl = s.split(' ')
    return sl[-1][1:-1]

def gera_listas(mbox, date):
    novatos = []
    antigos = []
    for i in mbox.iterkeys():
        m = mbox.get(i)
        email = retorna_email(m['from'])
        if gera_data(m['date']) < date:
            if not email in antigos:
                antigos.append(email)
        else:
            if not email in antigos:
                if not email in novatos:
                    novatos.append(Novato(email, m))
    return (antigos, novatos)

def verifica_tempo_resposta(novatos):
    for novato in novatos:
        mensagem_novato = novato.get_mensagem()
        for mensagem in mailbox.mbox('201104.mbox'):
            if mensagem_novato['subject'] in mensagem['subject']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
            elif mensagem['references'] != None and mensagem_novato['Message-ID'] in mensagem['References']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
            elif mensagem_novato['message-id'] == mensagem['in-reply-to']:
                td = gera_data(mensagem['date']) - gera_data(mensagem_novato['date'])
                novato.set_tempo_resposta(td)
    return novatos

def calcula_media_tempo_resposta(novatos):
    soma = 0
    for n in novatos:
        soma += n.get_tempo_resposta()
    return soma/len(novatos)

def media():
    date = datetime.datetime(2011, 4, 20)
    mbox = mailbox.mbox('jabref-devel.mbox')
    antigos, novatos = gera_listas(mbox, date)
    novatos = verifica_tempo_resposta(novatos)
    media = calcula_media_tempo_resposta(novatos)
    print(media)
