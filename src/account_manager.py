from queue import Queue
import threading
import datetime
from threading import Thread, BoundedSemaphore
from colorama import Fore, Back
from vote_bot import VoteBot
import time


max_connections = 2
semaphore = BoundedSemaphore(max_connections)


# A thread that produces data
def producer(out_q, account):
    semaphore.acquire()
    try:
        vote = VoteBot(account)
        vote.run()
    except Exception as e:
        print(Fore.RED + f"Teve erro. Testando com outro usuário...")
        semaphore.release()
        out_q.put(account)


# A thread that consumes data
def consumer(in_q, accounts):
    while True:
        data = in_q.get()
        print('consumer!', data)
        accounts[data] = datetime.datetime.now()
        print('accounts', accounts)



class AccountManager(object):
    def __init__(self, config):
        import pdb; pdb.set_trace()
        self.accounts = dict.fromkeys(config['credentials'], None)
        self.q = Queue(maxsize=max_connections)

    def run(self):
        Thread(target=consumer, args =(self.q, self.accounts)).start()
        for account, timestamp in self.accounts.items():
            t2 = Thread(target=producer, args =(self.q, account))
            t2.start()
