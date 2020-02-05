from sys import stdout, stdin, stderr, exit as sys_exit
from colorama import Fore as Font

def my_output(*args):
    for s in args:
        string = s
        if type(s) != type(""):
            string = str(s)
        stdout.write(string)

def my_error(_type, message, exiting=True):
    

def my_input(q, oneline=True):
    if oneline:
        stdin.readline()

