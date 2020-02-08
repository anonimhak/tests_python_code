from sys import stdout, stdin, stderr, exit as sys_exit
from colorama import Fore as Font
from typing import List

def my_output(*args):
    for s in args:
        string = s
        if type(s) != type(""):
            string = str(s)
        stdout.write(string)

def my_error(_type, message, exiting=True):
    pass    

def my_input(q, oneline=True):
    if oneline:
        stdin.readline()

def print_table_list(l: List[int]):
    for i in l:
        pass

def print_table_dict(_d):
    d = sorted(_d)
    stdout.write("--- Полігон частот ---"+"-"*50+"\n")
    stdout.write("| Індекс   |")
    for i in d:
        if len(str(i)) == 1: spaces = "  "
        elif len(str(i)) == 2: spaces = " "
        elif len(str(i)) == 3: spaces = ""
        stdout.write(" "+str(i)+spaces+" | ")
    stdout.write("\n| Частота  |")
    for n in d:
        i = _d[n]
        if len(str(i)) == 1: spaces = "  "
        elif len(str(i)) == 2: spaces = " "
        elif len(str(i)) == 3: spaces = ""
        stdout.write(" "+str(i)+spaces+" | ")
    stdout.write("\n"+"-"*72+"\n")

