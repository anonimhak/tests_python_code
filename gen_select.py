import socket as sock
from select import select

addr = []
to_read = {}
to_write = {}
tasks = []

def server():
    global addr
    server_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    server_socket.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 5555))
    server_socket.listen()

    while True:
        yield ("read", server_socket)
        client_socket, addr = server_socket.accept()
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ("read", client_socket)
        request = client_socket.recv(1024)
        print("Message from '{}' - {}".format(addr[0]+":"+str(addr[1]), request.decode()))
        response = "Hello '{}'\n".format(addr[0]+":"+str(addr[1]))
        response = response.encode()
        yield ("write", client_socket)
        client_socket.send(response)
    client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            read, write, _ = select(to_read, to_write, [])
            for sock in read:
                tasks.append(to_read.pop(sock))
            for sock in write:
                tasks.append(to_write.pop(sock))
        try:
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == "read":
                to_read[sock] = task
            if reason == "write":
                to_write[sock] = task
        except StopIteration: pass

tasks.append(server())
event_loop()
