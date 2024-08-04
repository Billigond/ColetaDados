from integracoes import Beatifullsoup


link="https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"
}

dados_site=Beatifullsoup.coletar_cotacao(link,headers)
print(dados_site)