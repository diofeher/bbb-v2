import time
import requests
from login_bot import login_bot
from vote_bot import VoteBot


class UserBot(object):
    def __init__(self, username, password, participant):
        self.username = username
        self.password = password
        self.participant = participant


    def run(self):
        print()
        session = login_bot(self.username, self.password)

        bot = VoteBot(session, self.participant)
        while True:
            print()
            bot.start_session()
            bot.generate_captcha()
            try:
                bot.captcha_verification()
            except TypeError as e:
                print('Captcha precisa ser adicionado na banco de imagens.')
                continue
            bot.vote()
