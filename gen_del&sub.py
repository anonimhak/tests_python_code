def coroutine(function):
    def wraper(*args, **kwargs):
        g = function(*args, **kwargs)
        g.send(None)
        return g
    return wraper

def sub_gen():
    while True:
        try:
            message = yield
            for i in message:
                yield i
        except StopIteration:
            yield "STOP !!!"
        else:
            break
    return "Return from sub gen"

@coroutine
def del_gen(sub):
    result = yield from sub
    print(result)

sg = sub_gen()
g = del_gen(sg)
