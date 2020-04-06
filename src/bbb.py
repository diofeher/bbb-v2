import requests
import time
import json
import datetime
from utils import cookie_string_to_mapping, read_configuration_file
from login_bot import login_bot
from vote_bot import VoteBot



if __name__ == "__main__":
    config = read_configuration_file()

    username = config['credentials']['username']
    password = config['credentials']['password']
    participant = config['participant']

    session = login_bot(username, password)
    started_time = datetime.datetime.now()
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
