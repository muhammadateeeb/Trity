# coding: utf-8
#!/usr/bin/env python
import sys, platform, subprocess, socket, time, os, urllib, platform, random, string, smtplib, requests, urllib2, getpass, zipfile
from urllib2 import urlopen
from termcolor import colored
from time import sleep
from getpass import getpass
from subprocess import call
sys.path.append('trity/')
from smtp import *
from sms import *
from gmail import *
from crafttable import *
from clickjacking import *
from info import *
from twitter import *
from whoisweb import *
from coder import *
from clone import *
from admin import *
from banner import *
from joke import *
from facebook import *
from quote import *
from anon import *
from web import *
from qr import *
from siteexists import *
from hex import *
from searchs import *
from zip import *
from emaill import *
try:
    import netifaces
    import scapy
    import readline
    import pip
    import pythonwhois
    import argparse
    import google
except ImportError:
    print (color.UNDERLINE + "\033[91m" + "You don't have some modules installed! \nPlease run install.py to install this tool fully! " + color.END)
    sys.exit()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
os.system('clear')

if str(platform.system()) != "Linux":
    sys.exit(f"{R}[!] {color.UNDERLINE}\033[91mYou are not using a Linux Based OS! Linux is a must-have for this script!{color.END}")

if not os.geteuid() == 0:
    sys.exit(f"{R}[!] {color.UNDERLINE}\033[91mMust be run as root. :/{color.END}")

if 'no' in open('agree.txt').read():  # take out the trity/
    print(f"{color.BOLD}Note that Trity is provided as is, and is a royalty-free open-source application.")
    agree = input(f"{G}{color.UNDERLINE}Do you agree to these terms and conditions?>{color.END}")
    
    if agree.lower() in ["yes", "y"]:
        print(f"{G}{color.UNDERLINE}Thanks!{color.END}")
        time.sleep(3)
        FILE = open("agree.txt", "w")  # take out the trity/
        FILE.write('yes')
        FILE.close()
    else:
        print(f"{R}{color.UNDERLINE}[!] You have to agree!{color.END}")
        time.sleep(1)
        sys.exit()

os.system('clear')
banner()
#============================================================#
#------------------- Onto the real stuff --------------------#
#============================================================#
def banner1():
    print ("")
    print (""+M+"|----- Made by _t0x1c aka toxic -----|")
    print (color.DARKCYAN +"|-----      Version: 3.0.1      -----|")
    print (color.WARNING + "|-----   1 tool - 35 choices    -----|")
    print (color.RED + "|-----  www.toxic-ig.github.io  -----|")
    print (color.PURPLE + "\n|----- A Warm Welcome to Trity! -----|")
    print (color.BLUE + "|----- Network Pentesting tool! -----|")
    print (color.YELLOW + "|----- Have Fun and Stay Legal! -----|")

time.sleep(0.1)
print ("")
time.sleep(0.1)
print (""+M+"|----- Made by _t0x1c aka toxic -----|")
time.sleep(0.1)
print (color.DARKCYAN + "|-----      Version: 3.0.1      -----|")
time.sleep(0.1)
print (color.WARNING + "|-----   1 tool - 35 choices    -----|")
time.sleep(0.1) 
print (color.RED + "|-----  www.toxic-ig.github.io  -----|")
time.sleep(0.1)
print (color.PURPLE + "\n|----- A Warm Welcome to Trity! -----|")
time.sleep(0.1)
print (color.BLUE + "|----- Awesome Pentesting tool! -----|")
time.sleep(0.1)
print (color.YELLOW + "|----- Have Fun and Stay Legal! -----|")
time.sleep(0.1)
r = requests.get('http://pastebin.com/raw/vYcBSV4w') 

if '3.1' not in r.text:
    print (''+R+'\nYou need to update! The newest version is: ' + color.BOLD + color.UNDERLINE + r.text + '\n')
else:
    print ('')
swear = "fuck", "shit", "nigga", "bitch", "dick", "pussy", "cunt", "nigger", "asshole", "ass"
spell = "helpp", "hellp", "bannerr", "baner", "emial", "HELP", "hwlp", "wesbite", "ehco", "anonymouss", "anonymouse", "toool", "tooll", "carft", "Info", "spooof", "spooff", "ecnode", "decde", "encde", "craftt", "qoute", "sitexists", "hlep", "claer"
def tritymain():
    while True:
        try:
            main = input('' + G + '' + color.BOLD + color.UNDERLINE + 'Tri>' + color.END)
            
            if main in swear:
                print("" + R + "[!] " + color.UNDERLINE + "\033[91m" + "Watch your language!" + color.END)
            elif main in spell:
                print("" + R + "[!] " + color.UNDERLINE + "\033[91m" + "Do you know how to spell?!" + color.END)
            elif main == "joke":
                joke()
            elif main == "info":
                info()
            elif main == "help":
                print("" + W + "+----------------------------+")
                # ... rest of your "help" code
            elif main == "spoof mac":
                # ... rest of your "spoof mac" code
            elif main == "sms":
                sms()
            elif main == "encode base64":
                encode()
            elif main == "decode base64":
                decode()
            elif main == "email":
                smtp()
            # ... rest of your elif conditions
            elif main == "clear":
                os.system('clear')
            elif main == "exit":
                print("" + G + "[*] " + color.UNDERLINE + "\033[91m" + "Exiting..." + color.END)
                print("" + G + "[*] " + color.UNDERLINE + "\033[92m" + "Goodbye!" + color.END)
                time.sleep(0.2)
                sys.exit()
            elif main == "":
                print("" + R + "[!] " + color.UNDERLINE + "\033[91m" + "Please enter an option!" + color.END)
            else:
                print("" + R + "[!] " + color.UNDERLINE + "\033[91m" + "That is not an option!" + color.END)
        except KeyboardInterrupt:
            print("\n")
            tritymain()

tritymain()

