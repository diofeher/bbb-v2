import requests, re
from urllib.parse import urlparse

headerspool = {
    "Host": "gshow.globo.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20101101 Firefox/74.0.8",
  "Content-Type": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate",
  "Connection": "close"
}
def get_pool():
    while True:
        urlgetpool = input('Cole a URL da votação:')
        try:
            x = requests.get(urlgetpool, headers=headerspool)
            resp1 = x.text
            resource_id = re.findall('resource_id":"(.+?)"', resp1)
            nomes_part = re.findall('type":"ImageObject","name":"(.+?)_votacaobbb20', resp1)
            print(resource_id[0])
            if resource_id[0]:
                return resource_id[0],nomes_part[0],nomes_part[1],nomes_part[2]
                break
        except:
            print('Confirme a URL da votação')
            pass

def get_parts(url):
        urlgetpool = url
        try:
            x = requests.get(urlgetpool, headers=headerspool)
            resp1 = x.text
            nomes_part = re.findall('type":"ImageObject","name":"(.+?)_votacaobbb20', resp1)
            return nomes_part[0],nomes_part[1],nomes_part[2]
        except:
            pass
