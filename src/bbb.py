import requests
import time
import json
import datetime
import sys
from utils import cookie_string_to_mapping, read_configuration_file
from login_bot import login_bot
from vote_bot import VoteBot
from colorama import Fore, Back
from get_pool import get_pool
from vote_bot import getpool
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
    print()
    while True:
        try:
           opcaovoto = int(sys.argv[1])
        except:
                opcaovoto = input(Fore.GREEN + f"Em quem quer votar? ("+getpool[1]+" = 1 /"+getpool[2]+" = 2 /"+getpool[3]+" = 3): ")

        try:
            participant = int(opcaovoto)
            if participant > 0 and participant < 4:
                nomevoto = getpool[participant]
                if nomevoto == "babu":
                    nomevoto = "babu :'("
                print("Votando na opção:",opcaovoto," ",nomevoto)
                time.sleep(5)
                break
        except ValueError:
            pass
    while True:
        for cred in config['credentials']:
            username = cred['username']
            password = cred['password']
            user_session(username, password)
