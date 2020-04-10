# coding: utf-8
import requests
import time
import json
import datetime
import sys
from user_bot import UserBot
from account_manager import AccountManager
from utils import cookie_string_to_mapping, read_configuration_file


if __name__ == "__main__":
    config = read_configuration_file()
    manager = AccountManager(config['credentials'])
    manager.run()
