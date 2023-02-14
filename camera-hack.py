from colorama import Fore, Back, Style
from time import sleep
from os import system
print (Fore.BLUE, Back.RED, "welcome!!", Style.RESET_ALL)
sleep(1)
system("clear")
print (Fore.RED, Back.CYAN, "                😈cyber boy😈")
print (Fore.RED, Back.CYAN, "                  👻@filter_code👻")
print (Style.RESET_ALL)
sleep(1)
print (Fore.GREEN, Back.BLUE,"")
print ("   1:japan")
print ("   2:Ameika🤢")
print ("   3:qatar")
print (Style.RESET_ALL, " \n \n \n \n \n")
code = input('///>>>')
if code=='1':
 japan = open("japan.txt", "r")
 A = japan.read()
 print (Style.RESET_ALL, Fore.GREEN, "")
 print (" hacked!! \n plase wait!!", Style.RESET_ALL)
 sleep(3)
 print (Fore.RED, A)

if code=='2':
 amrika = open("amrika.txt", "r")
 B = amrika.read()
 print (Style.RESET_ALL,Fore.GREEN, "")
 print (" hacked!! \n plase wait!!", Style.RESET_ALL)
 sleep(3)
 B = amrika.read()
if code=='3':
 brazil = open("brazil.txt", "r")
 C = brazil.read()
 print (Style.RESET_ALL,Fore.GREEN, "")
 print (" hacked!! \n plase wait!!", Style.RESET_ALL)
 sleep(3)
 print (Fore.RED, C)
