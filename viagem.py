from bs4 import BeautifulSoup
import requests
import re

URL = "https://brasilescola.uol.com.br/gramatica/viagem-ou-viajem.htm"
padrao = re.compile(r"^Viagem", re.IGNORECASE)


def pesquisar_viagem():
    
    return 

def quando_usar_viagem(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "viagem":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('h1', text = padrao).find_next('p').find_next('p').find_next('p')

        print(paragrafo.text)
    return executado