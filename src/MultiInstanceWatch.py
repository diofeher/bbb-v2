import pyfiglet
import colorama
from colorama import Fore, Back
import os
import threading
atualizacao = 5.0 #segundos
colorama.init(autoreset=True)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def line_count(fname):
    return sum(1 for line in open(fname))
   
def printit():
    threading.Timer(atualizacao, printit).start()
    cls() 
    ascii_banner = pyfiglet.figlet_format("BBB BOT v3")
    print(Fore.GREEN + ascii_banner)
    votox = line_count("total.log")
    print(Fore.RED + "[*]Total: "+ str(votox))
    banner = pyfiglet.figlet_format(str(votox))
    print(Fore.GREEN +banner)
    
cls() 
printit()
