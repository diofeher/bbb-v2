import requests, re
from urllib.parse import urlparse
from colorama import Fore, Back
headerspool = {
    "Host": "gshow.globo.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20101101 Firefox/74.0.8",
  "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate",
  "Connection": "close"
}

print(Fore.WHITE + f"")
def get_urlvotacao():
    try:
        urlglobo = "https://gshow.globo.com/realities/bbb/"
        x = requests.get(urlglobo, headers=headerspool)
        respg = x.text
        urlvotacao = re.findall('url":"https://gshow.globo.com/realities/bbb/bbb20/votacao/(.+?)"', respg)
        urlvotacao = "https://gshow.globo.com/realities/bbb/bbb20/votacao/"+urlvotacao[0]
        return urlvotacao
    except:
        print('Nao foi possivel pegar a URL da votação')
        return input(Fore.BLUE + f"Cole a URL da votação:")

def get_pool():
    urlgetpool = get_urlvotacao()
    while True:        
        try:
            x = requests.get(urlgetpool, headers=headerspool)
            resp1 = x.text
            resource_id = re.findall('resource_id":"(.+?)"', resp1)
            nomes_part = re.findall('type":"ImageObject","name":"(.+?)_votacaobbb20', resp1)
            if resource_id[0]:
                print("Votação detectada")
                return resource_id[0],nomes_part[0],nomes_part[1],nomes_part[2]
                break
        except:
            print(Fore.RED + f"Confirme a URL da votação")
            urlgetpool = input(Fore.BLUE + f"Cole a URL da votação:")
            pass


