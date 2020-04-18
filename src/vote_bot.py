# coding: utf-8
import sys
import random
import copy
import requests
import json
import urllib.parse
import time
import colorama
from utils import resource_path, save_image, cookie_string_to_mapping
from proof_of_work import break_proof_of_work
from compare_images import compare
from errors import GloboBlockingException
from bbb_logging import vote_logger
from colorama import Fore, Back
from pools import get_pool
colorama.init(autoreset=True)

HASHZEROS_LIMIT = 6
VOTES = 0
# getpool = get_pool()
# POOL = getpool[0]
POOL = '9489daaa-15ee-4a2e-8e8d-22391a58e23c'
ROYALE_URL = 'royale.globo.com'
MAX_SECONDS_TO_WAIT = 623 # Dividido por 100. 6.23 segundos ---> Não recomendo mudar.
random_decimal1 = random.randint(325, MAX_SECONDS_TO_WAIT)/100
random_decimal2 = random.randint(325, MAX_SECONDS_TO_WAIT)/100
random_decimal3 = random.randint(325, MAX_SECONDS_TO_WAIT)/100
random_decimal4 = random.randint(325, MAX_SECONDS_TO_WAIT)/100
CAPTCHA_URL = f'https://{ROYALE_URL}/polls/{POOL}/session'
CAPTCHA_VERIFY_URL = 'http://captcha.globo.com/api/challenge/verify'
CAPTCHA_GENERATE_URL = 'https://captcha.globo.com/api/challenge/generate'
VOTE_URL = f'https://{ROYALE_URL}/polls/{POOL}/votes'


class VoteBot(object):
    def __init__(self, session, participant):
        self.appId = ''
        self.captchaSession = ''
        self.captchaToken = ''
        self.captchaSessionToken = ''
        self.captchaVerificationToken = ''
        self.symbol = ''
        self.participant = participant - 1
        self.option = 0
        self.computedVotes = 0
        self.hashcashZeros = 0
        self.session = session
        self.headers = {
            'content-type': 'text/plain;charset=UTF-8',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'Host': 'royale.globo.com',
            'origin': 'https://gshow.globo.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'x-verified': 'false',
        }

        self.hashcash = ''
        self.hashTime = ''


    def start_session(self):
        print('[+] Iniciando configuração de sessão...')

        params = {
            'zeros': self.hashcashZeros,
        }

        time.sleep(random_decimal1)
        response = self.session.get(
            CAPTCHA_URL,
            headers=self.headers,
            params=params
        )
        response_data = response.json()

        self.appId = response_data['configuration']['appId']
        self.captchaSession = response_data['session']
        self.hashcash = response.headers.get('x-hashcash', '')


    def generate_captcha(self, wait_time=random_decimal2):
        print('[+] Pegar captcha da Globo')

        headers = copy.copy(self.headers)
        headers['content-type'] = 'application/x-www-form-urlencoded'

        params = {
            'appId': self.appId,
            'runtime': '1.1.5',
        }

        time.sleep(wait_time)
        response = self.session.post(
            CAPTCHA_GENERATE_URL,
            params=params,
            headers=headers
        )

        response_data = response.json()

        self.symbol = response_data['data']['symbol']
        self.captchaSessionToken = response_data['sessionToken']
        save_image(resource_path('images/'), self.symbol, response_data['data']['image'])
        return response_data['data']


    def captcha_verification(self):
        print(f"[+] Procurando captcha no banco de dados: {self.symbol}")
        self.option = compare(self.symbol)
        y = 30
        x = 53 * self.option + 25
        print(f"\tPosição de clique (X: {x}, Y: {y})")

        params = {
            'appId': self.appId,
            'runtime': '1.1.5',
        }

        payload_data = {
            'sessionToken': self.captchaSessionToken,
            'input': {
                'clickX': x,
                'clickY': y,
            }
        }


        data = {
            'payload': json.dumps(payload_data).replace(' ', '')
        }

        headers = copy.copy(self.headers)
        del headers['content-type']

        time.sleep(random_decimal3)
        response = self.session.post(
            CAPTCHA_VERIFY_URL,
            headers=headers,
            params=params,
            data=data
        )

        verificationToken = response.json()['verificationToken']
        self.captchaVerificationToken = verificationToken.replace('+', '-').replace('/', '_').replace('=', '')


    def vote(self):
        print(f'[+] Votando... Posição: {self.option}, Hashcash: {self.hashcash}, Zeros:{self.hashcashZeros}')
        if self.hashcashZeros == 0:
            nonce = 0
        else:
            nonce = break_proof_of_work(self.hashcash, self.hashcashZeros)

        params = {
            'captcha-token': self.captchaVerificationToken,
            'challenge': self.captchaSession,
            'nonce': nonce,
        }

        data = f'{{"optionId":{self.participant}}}'

        headers = {
            'Host': 'royale.globo.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
            'X-Verified': 'false',
            'Content-Type': 'text/plain',
            'Origin': 'https://globoesporte.globo.com',
        }

        time.sleep(random_decimal4)
        response = self.session.post(
            VOTE_URL,
            headers=headers,
            params=params,
            data=data
        )

        hashcashZeros = response.headers.get('x-hashcash-required-zeros', '')
        if hashcashZeros:
            self.hashcashZeros = hashcashZeros

            if int(hashcashZeros) >= HASHZEROS_LIMIT:
                print(Fore.RED + f"[-] A Globo está pedindo uma proof of work gigante ({hashcashZeros}) pra esse usuário, tentando o próximo...")
                raise GloboBlockingException

        if response.status_code == 200:
            self.computedVotes += 1
            print(Fore.GREEN + f"[+] Voto computado! Total de votos: {self.computedVotes}")
            vote_logger.info(f"[+] Voto computado! {self.session.cookies}")
        elif response.status_code == 403:
            print(Fore.RED + "[-] Erro de autorização ou captcha inválido!")
        elif response.status_code == 406:
            print(Fore.RED + "[-] Tentativa de bloqueio de voto, erro 406.")
            raise GloboBlockingException
        elif response.status_code == 422:
            print(Fore.RED + "[-] Proof of Work Inválido.")
        elif response.status_code == 410:
            print(Fore.RED + "[-] Votação Fechada.")
        elif response.status_code == 503:
            print("[-] Serviço indisponível.")

        else:
            print(Fore.RED + f"[-] Erro desconhecido {response.status_code}, Resposta: {response.text}")
