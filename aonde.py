from bs4 import BeautifulSoup
import requests
import re

URL = "https://ead.pucgoias.edu.br/blog/aonde-ou-onde"
padrao = re.compile(r"^Enquanto", re.IGNORECASE)


def pesquisar_aonde():
    
    return 

def quando_usar_aonde(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "aonde":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('p', text = padrao)

        print(paragrafo.text)
    return executado