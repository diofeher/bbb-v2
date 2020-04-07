import requests
import time
import json
import datetime
from utils import cookie_string_to_mapping, read_configuration_file
from login_bot import login_bot
from vote_bot import VoteBot
from colorama import Fore, Back


def user_session(username, password):
    print()
    try:
        session = login_bot(username, password)
        bot = VoteBot(session, participant)
        while True:
            print()
            try:
                bot.start_session()
                bot.generate_captcha()
                try:
                    bot.captcha_verification()
                except TypeError as e:
                    print('Captcha precisa ser adicionado na banco de imagens.')
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

    participant = config['participant']
    while True:
        for cred in config['credentials']:
            username = cred['username']
            password = cred['password']
            user_session(username, password)
