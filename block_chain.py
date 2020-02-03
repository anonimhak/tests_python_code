from os import listdir
from sys import argv, exit as sexit
from hashlib import md5
from json import dump, load
from colorama import Fore as Font

def create_block(path_to_blocks):
    blocks = listdir(path_to_blocks):
    for bloc in blocks:
        int(block)
    blocks = blocks.sort()
    hash_back_block = md5()
    data = {"title": input("Title: "),
            "content": input("Content: "),
            "tags": input("Tags: ").split(", "),
            "hash": hash_back_block}

def main():
    for arg in argv:
        if arg.endswith(".py"): continue
        elif arg == "get":
            get();sexit(0)
        elif arg == "check":
            check();sexit(0)
        elif arg == "add":
            add();sexit(0)
        elif arg == "set":
            set(argv[argv.index("set"):])

if __name__ == "__main__":
    main()
