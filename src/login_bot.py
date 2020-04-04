# coding: utf-8
import requests
import json


def login_bot(email, password):
    headers = {
        "Host": "login.globo.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Content-Type": "application/json",
        "Origin": "http://login.globo.com",
        "Connection": "close",
    }

    data = {
        "payload":{
            "email":email,
            "password":password,
            "serviceId":1
        },
        "captcha":"",
    }

    session = requests.Session()
    print("[+] Fazendo login...")
    response = session.post('https://login.globo.com/api/authentication', headers=headers, json=data)
    HIDDEN = 80
    if response.status_code != 200:
        raise Exception("Login não foi feito com sucesso, tente de novo.")
    else:
        print(f"[+] Login feito com sucesso... ID: {response.cookies['GLBID'][:-HIDDEN]}{'*'*HIDDEN}")

    return session
