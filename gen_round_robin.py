def gen_s(string):
    for i in string:
        yield i

def gen_n(numbers):
    for i in range(numbers):
        yield i

tasks = [ gen_s("Hello world"), gen_n(16) ]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration: pass

