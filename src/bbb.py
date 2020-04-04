from vote_bot import VoteBot
import requests
from utils import cookie_string_to_mapping, read_configuration_file
from login_bot import login_bot
import json
import datetime

import logging


if __name__ == "__main__":
    config = read_configuration_file()

    username = config['credentials']['username']
    password = config['credentials']['password']
    participant = config['participant']

    session = login_bot(username, password)
    started_time = datetime.datetime.now()
    bot = VoteBot(session, participant)
    while True:
        bot.start_session()
        print()
        bot.generate_captcha()
        try:
            bot.captcha_verification()
        except Exception as e:
            print(e)
            print('Captcha precisa ser adicionado na banco de imagens.')
            continue
        bot.vote()
        print(f'Started time: {started_time}. Now: {datetime.datetime.now()}')
