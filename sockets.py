import socket as sock

server_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
server_socket.setsockopt(sock.SOL_SOCKET, sock.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 5555))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    while True:
        request = client_socket.recv(1024)
        print("Message from '{}' - {}".format(addr[0]+":"+str(addr[1]), request.decode()))
        response = "Hello '{}'\n".format(addr[0]+":"+str(addr[1]))
        response = response.encode()
        client_socket.send(response)
    client_socket.close()

server_socket.close()

