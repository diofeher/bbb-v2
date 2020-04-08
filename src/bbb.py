# coding: utf-8
import requests
import time
import json
import datetime
from utils import cookie_string_to_mapping, read_configuration_file, save_image
from login_bot import login_bot
from vote_bot import VoteBot
from colorama import Fore, Back
from pools import get_pool
from vote_bot import getpool
from random import randint
import sys


def user_session(username, password, participant):
    print()
    try:
        session = login_bot(username, password)

        bot = VoteBot(session, participant)
        while True:
            print()
            try:
                bot.start_session()
                captcha = bot.generate_captcha()
                try:
                    bot.captcha_verification()
                except TypeError as e:
                    icon = captcha['symbol']
                    save_image('./src/images_unclassified/', f'{icon}_{randint(10000, 99999)}', captcha['image'])
                    print('[-] Captcha adicionado a lista de não classificado, para aprimorar a quebra das capthas confira o README')
                    continue
                bot.vote()
            except requests.exceptions.ConnectionError as e:
                print("[-] Servidor da Globo sobrecarregado... Tentando de novo em 1 minuto.")
                time.sleep(60)
    except Exception as e:
        print(e)
        print(Fore.RED + f"Teve erro. Testando com outro usuário...")



if __name__ == "__main__":
    config = read_configuration_file()
    print()
    while True:
        for cred in config['credentials']:
            username = cred['username']
            password = cred['password']
            user_session(username, password, config['participant'])
