# coding: utf-8
from utils import read_configuration_file
from account_manager import AccountManager


if __name__ == "__main__":
    config = read_configuration_file()
    manager = AccountManager(config['credentials'], config['participant'])
    manager.run()
