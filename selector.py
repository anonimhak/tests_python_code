import socket
from selectors import DefaultSelector, EVENT_READ

selector = DefaultSelector()
addr = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 5555))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=EVENT_READ, data=accept_connection)

def accept_connection(sock):
    global addr
    client_socket, addr = sock.accept()

    selector.register(fileobj=client_socket, events=EVENT_READ, data=send_message)

def send_message(sock):
    request = sock.recv(1024)
    if request:
        print("Message from '{}' - {}".format(addr[0]+":"+str(addr[1]), request.decode()))
        response = "Hello '{}'\n".format(addr[0]+":"+str(addr[1]))
        response = response.encode()
        sock.send(response)
    else:
        selector.unregister(sock)
        sock.close()

def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == "__main__":
    server()
    event_loop()

