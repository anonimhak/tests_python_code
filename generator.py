from random import randint

def gen():
    while True:
        yield randint(0, 100)

g = gen()
next(g)

print(next(g))

