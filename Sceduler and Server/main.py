from pyscript import display
import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 1234
token_queue = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

while True:
    client_socket, address = server_socket.accept()
    print("Connection from", address)
    data = client_socket.recv(1024)
    data = data.decode()
    token_queue.append(data)
    client_socket.close()
    if len(token_queue)<4:
        for _ in range(4-len(token_queue)):
            token_queue.append(0) 
    display(token_queue[0], target="token_1", append=False)
    display(token_queue[1], target="token_2", append=False)
    display(token_queue[2], target="token_3", append=False)
    display(token_queue[3], target="token_4", append=False)
