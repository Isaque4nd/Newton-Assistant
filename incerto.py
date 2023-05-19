from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.dicio.com.br/incerto-ou-inserto/"
padrao = re.compile(r"^Incerto", re.IGNORECASE)


def pesquisar_incerto():
    
    return 

def quando_usar_incerto(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "incerto":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('h1', text = padrao).find_next('p')

        print(paragrafo.text)
    return executado