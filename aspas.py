from bs4 import BeautifulSoup
import requests
import re

URL = "https://mundoeducacao.uol.com.br/gramatica/aspas.htm"
padrao = re.compile(r"^Aspas", re.IGNORECASE)


def pesquisar_aspas():
    
    return 

def quando_usar_aspas(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "aspas":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('h1', text = padrao).find_next('div')

        print(paragrafo.text)
    return executado