import threading
import datetime
import time
from queue import Queue
from threading import Thread, BoundedSemaphore
from colorama import Fore, Back
from user_bot import UserBot
from utils import read_configuration_file


config = read_configuration_file()
MAX_CONNS = config['contasEmParalelo'] or 1
RETRY_TIME = 30 * 60  # 30 minutes * secs
semaphore = BoundedSemaphore(MAX_CONNS)


def producer(out_q, data, participant):
    username = data['username']
    password = data['password']
    semaphore.acquire()
    try:
        bot = UserBot(username, password, participant)
        bot.run()
    except Exception as e:
        print(f"{Fore.RED} Teve erro em {username}. {e} Testando com outro usuário...")
        semaphore.release()
        out_q.put(username)


# A thread that consumes data
def consumer(in_q, accounts, participant):
    while True:
        username = in_q.get()
        accounts[username]['timestamp'] = datetime.datetime.now()
        for username, creds in accounts.items():
            diff = datetime.datetime.now() - creds['timestamp']
            if diff.seconds > RETRY_TIME:
                Thread(
                    target=producer,
                    args=(in_q, creds, participant)
                ).start()
        time.sleep(60)


class AccountManager(object):
    def __init__(self, credentials, participant):
        accs = {}
        for creds in credentials:
            username = creds['username']
            accs[username] = creds
            accs[username]['timestamp'] = datetime.datetime.now()
        self.accounts = accs
        self.participant = participant
        self.q = Queue(maxsize=MAX_CONNS)

    def run(self):
        t1 = Thread(
            target=consumer,
            args=(self.q, self.accounts, self.participant)
        )
        t1.start()

        for _, creds in self.accounts.items():
            t2 = Thread(
                target=producer,
                args=(self.q, creds, self.participant)
            )
            t2.start()
