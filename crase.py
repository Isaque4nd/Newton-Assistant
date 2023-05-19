from bs4 import BeautifulSoup
import requests
import re

URL = "https://brasilescola.uol.com.br/gramatica/crase.htm#:~:text=5%20-%20Exercícios%20resolvidos-,Quando%20usar%20a%20crase%3F,a%20loja%20%3D%20Vamos%20à%20loja."
padrao = re.compile(r"^Quando", re.IGNORECASE)


def pesquisar_crase():
    
    return 

def quando_usar_crase(acao, objeto, _):
    executado = False

    if acao in [ "usar", "usamos" ] and objeto == "crase":
        executado = True
        resposta = requests.get(URL)
        soup = BeautifulSoup(resposta.content, 'html.parser')

        paragrafo = soup.find('h2', text = padrao).find_next('p')

        print(paragrafo.text)
    return executado