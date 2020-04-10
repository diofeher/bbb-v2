from utils import save_image, read_configuration_file
from vote_bot import CAPTCHA_GENERATE_URL, VoteBot
import time
import requests
import random
from login_bot import login_bot
import json
import datetime


SAVE_PATH = "./src/classifier/images/"


if __name__ == "__main__":
    config = read_configuration_file()

    username = config['credentials'][0]['username']
    password = config['credentials'][0]['password']
    participant = config['participant']

    session = login_bot(username, password)
    started_time = datetime.datetime.now()
    bot = VoteBot(session, participant)
    bot.start_session()
    while True:
        print()
        captcha = bot.generate_captcha(wait_time=3.5)
        save_image(SAVE_PATH, f"{captcha['symbol']}_{random.randint(10000, 99999)}", captcha['image'])
        print(f'Started time: {started_time}. Now: {datetime.datetime.now()}')
