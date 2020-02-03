import multiprocessing as mp
from time import sleep

def print_nums():
    from colorama import Fore as Font
    num = 1
    while True:
        print(Font.YELLOW, num)
        num += 1
        sleep(1)

def print_messages():
    from colorama import Fore as Font
    count = 0
    while True:
        if count % 3 == 0:
            print(Font.BLUE, "Hello "+str(count))
        count += 1
        sleep(1)

def main():
    processs: list = [
        mp.Process(target=print_nums),
        mp.Process(target=print_messages)
    ]
    for process in processs:
        process.start()

if __name__ == "__main__":
    main()

