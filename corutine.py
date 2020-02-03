
def cor():
    while True:
        data = yield
        print( data )

c = cor()
next(c)

print(c.send("Data test"))

