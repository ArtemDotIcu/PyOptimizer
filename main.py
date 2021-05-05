# python3
import time
import os
import subprocess
import getpass
from colorama import Fore

# variables
username = getpass.getuser()
temp_del_dir = r'c:\windows\temp'
prefetch_del_dir = r'c:\windows\Prefetch'
success = 0
fails = 0

# Welcome
def welcome():
    print("""
  _____        ____        _   _           _              
 |  __ \      / __ \      | | (_)         (_)             
 | |__) |   _| |  | |_ __ | |_ _ _ __ ___  _ _______ _ __ 
 |  ___/ | | | |  | | '_ \| __| | '_ ` _ \| |_  / _ \ '__|
 | |   | |_| | |__| | |_) | |_| | | | | | | |/ /  __/ |   
 |_|    \__, |\____/| .__/ \__|_|_| |_| |_|_/___\___|_|   
         __/ |      | |                                   
        |___/       |_|                                   
    
    """)
    time.sleep(0.8)
    print("Welcome " + username)
    time.sleep(5)

# temp
def temp():
    process = subprocess.Popen('rmdir /S /Q {}'.format(temp_del_dir), shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        success = + 1
    else:
        print('Fail: Unable to Clean Windows Temp Folder')
        fails = + 1

# prefetch
def prefetch():
    process = subprocess.Popen('rmdir /S /Q {}'.format(prefetch_del_dir), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        success = + 1
    else:
        print('Fail: Unable to Clean Windows Prefecth Folder')
        fails = + 1

# optimizer
def optimizer():
    time.sleep(2)
    print(Fore.RED + "Starting optimize" + Fore.RESET)
    time.sleep(1.2)
    print("Clearing temp files...")
    temp()
    time.sleep(0.1)
    print("Clearing prefetch files...")
    prefetch()
    time.sleep(0.1)
    print("Done.")
    time.sleep(5)
    exit()

# clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#code
clear()
welcome()
clear()
optimizer()