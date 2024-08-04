import requests as rq
from bs4 import BeautifulSoup

# Coletar o Site.
def coletar_site(link,headers):
    
    try:
        dados=rq.get(link,headers=headers)
        site=BeautifulSoup(dados.text,"html.parser")
        return site.prettify()
    
    except Exception as e:
        return e
    
# Coletar o Título do site.    
def coletar_titulo_site(link,headers):
    
    try:
        dados=rq.get(link,headers=headers)
        site=BeautifulSoup(dados.text,"html.parser")
        return site.find("title")
    
    except Exception as e:
        return e

#Coletar a cotação do dolar.
def coletar_cotacao(link, header):
    try:
        # Faz a requisição para o link fornecido com o cabeçalho
        dados = rq.get(link, headers=header)
        # Analisa o conteúdo HTML da resposta
        site = BeautifulSoup(dados.text, "html.parser")
        # Encontra o elemento específico com a classe fornecida
        cotacao = site.find("span", class_="AP7Wnd")
        
        # Verifica se a cotação foi encontrada
        if cotacao:
            return cotacao.text
        else:
            return "Cotação não encontrada."
    
    except rq.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"

# Coletar dados do Elemento no Input.
def encontrar_input(link,headers):
    
    try:
        dados=rq.get(link,headers=headers)
        site=BeautifulSoup(dados.text,"html.parser")
        return site.find_all("input")
    except Exception as e:
        return e
