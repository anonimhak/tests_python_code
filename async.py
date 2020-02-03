import asyncio as aio
from colorama import Fore as Font

async def print_nums():
    num = 1
    while True:
        print(Font.YELLOW, num)
        num += 1
        await aio.sleep(1)

async def print_message():
    count = 0
    while True:
        if count & 3 == 0:
            print(Font.BLUE, "Hello "+str(count))
        count += 1
        await aio.sleep(1)

async def main():
    tasks: list = [
        aio.create_task(print_nums()),
        aio.create_task(print_message())
    ]
    await aio.gather(*tasks)

if __name__ == "__main__":
    try: aio.run(main())
    except KeyboardInterrupt: pass

