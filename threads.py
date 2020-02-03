import threading as th
from time import sleep
from colorama import Fore as Font

def print_nums():
    num = 1
    while True:
        print(Font.BLUE, num)
        num += 1
        sleep(1)

def print_message():
    count = 0
    while True:
        if count % 3 == 0:
            print(Font.YELLOW, "Hello "+str(count))
        count += 1
        sleep(1)

def main():
    threads = [
        th.Thread(target=print_nums),
        th.Thread(target=print_message)
    ]

    for thread in threads:
        thread.start()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: pass

