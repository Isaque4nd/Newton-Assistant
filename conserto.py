from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.todamateria.com.br/conserto-concerto/"
padrao = re.compile(r"^As", re.IGNORECASE)


def pesquisar_conserto():
    
    return 

def quando_usar_conserto(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "conserto":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('p', text = padrao)

        print(paragrafo.text)
    return executado