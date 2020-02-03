import socket
from select import select

tasks = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 5555))
server_socket.listen()

addr = []

def accept_connection(sock):
    global addr
    client_socket, addr = sock.accept()
    tasks.append(client_socket)

def send_message(sock):
    request = sock.recv(1024)
    if request:
        print("Message from '{}' - {}".format(addr[0]+":"+str(addr[1]), request.decode()))
        response = "Hello '{}'\n".format(addr[0]+":"+str(addr[1]))
        response = response.encode()
        sock.send(response)
    else:
        sock.close()

def event_loop():
    while True:
        redy_to_read, _, _ = select(tasks, [], [])
        for sock in redy_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)

if __name__ == "__main__":
    tasks.append(server_socket)
    event_loop()

