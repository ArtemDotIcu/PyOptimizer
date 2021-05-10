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
user_temp_del_dir = r'c:\%temp%'

windows = 0


# clear downloads
def downloads():
    time.sleep(0.1)
    clear()
    print("Soon...")
    time.sleep(5)
    clear()
    welcome()


# clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# downloads - soon
def windows_cleaner():
    time.sleep(0.15)
    clear()
    time.sleep(0.1)
    print("Starting cleanmgr...")
    if os.name == 'nt':
        os.system("cleanmgr")
    else:
        print("You are non windows user, so you can use Windows cleaner.")
    time.sleep(5)
    clear()
    welcome()


# about
def about():
    time.sleep(0.08)
    clear()
    time.sleep(0.12)
    print(Fore.LIGHTBLUE_EX + "     < About / me >" + Fore.RESET)
    time.sleep(0.15)
    print("""

    Hi, I’m @ArtemDotIcu
    I’m currently learning Python3
    This is my first "big" Python tool
    How to reach me, discord: ArtemDotIcu | NT#1337
    """)
    time.sleep(15)
    clear()
    welcome()


# temp
def temp():
    process = subprocess.Popen('rmdir /S /Q {}'.format(temp_del_dir), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        time.sleep(0.1)
    else:
        print('Fail: Unable to Clean Windows Temp Folder')


# temp
def user_temp():
    process = subprocess.Popen('rmdir /S /Q {}'.format(user_temp_del_dir), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        time.sleep(0.1)
    else:
        print('Fail: Unable to Clean User Temp Folder')


# prefetch
def prefetch():
    process = subprocess.Popen('rmdir /S /Q {}'.format(prefetch_del_dir), shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _ = process.communicate()
    return_code = process.returncode
    if return_code == 0:
        time.sleep(0.1)
    else:
        print('Fail: Unable to Clean Windows Prefecth Folder')


# optimizer
def optimizer():
    time.sleep(0.12)
    clear()
    time.sleep(2)
    print(Fore.RED + "\nStarting optimize" + Fore.RESET)
    time.sleep(1.2)
    print("Clearing temp files...")
    temp()
    time.sleep(0.1)
    print("Clearing user temp files...")
    user_temp()
    time.sleep(0.1)
    print("Clearing prefetch files...")
    prefetch()
    time.sleep(0.1)
    print("Done.")
    time.sleep(5)
    clear()
    welcome()


def wincheck():
    time.sleep(0.1)
    if os.name == 'nt':
        time.sleep(0.4)
    else:
        print("Windows is not detected\nPlease note PyOptimizer work only on windows.")
        print("PyOptimizer will start anyway in 10seconds.")
        time.sleep(10)


def credit():
    print("""

        ╔═══════════════════════════════════╗
        ║ Made with love by ArtemFromNights ║
        ╠═══════════════════════════════════╣
        ║       github.com/artemdoticu      ║
        ╚═══════════════════════════════════╝

    """)
    time.sleep(3.8)
    clear()


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
    print("""
    
    
    1. Clear junk files     4. Clear downloads
    2. Windows cleaner      5. Exit
    3. About                
    
    """)
    menu = input("1-3: ")
    time.sleep(2)
    if menu == "1":
        optimizer()
    else:
        if menu == "2":
            windows_cleaner()
        else:
            if menu == "3":
                about()
            else:
                if menu == "4":
                    downloads()
                else:
                    if menu == "5":
                        exit()
                    else:
                        time.sleep(0.5)
                        print(Fore.RED + "\nInvalid argument.")
                        print("Please retry." + Fore.RESET)
                        time.sleep(5)
                        clear()
                        welcome()


# code
clear()
credit()
clear()
wincheck()
clear()
welcome()
# no sense --->
clear()
credit()
exit()
