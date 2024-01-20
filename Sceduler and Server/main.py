import socket
import json
import multiprocessing
from gui import gui

global queue 
TCP_IP = "127.0.0.1"
TCP_PORT = 1234
queue = []

def insert_token(token):
    global queue
    queue.append(token)

def remove_token():
    global queue
    if len(queue)==0:
        print("No tokens")
        return 0
    return queue.pop(0)

def prempt_token(token):
    global queue
    if len(queue)==0:
        print("No tokens")
        return 0
    queue.append(queue.pop(queue.index(token)))

def fcs_scheduler():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((TCP_IP, TCP_PORT))
    server_socket.listen(1)
    print("Server is Up")
    while True:
        client_socket, address = server_socket.accept()
        print("Connection from", address)
        data = client_socket.recv(1024)
        data = data.decode()
        if data == "next_token":
            token = remove_token()
        elif data == "hold_token":
            if len(queue)==0:
                print("No tokens")
                continue
            prempt_token(queue[0])
        elif data[0].isnumeric():
            token = client_socket.recv(1024)
            token = token.decode()
            insert_token(data)  
        print(queue)
        fp=open("data.json","w")
        json.dump(queue[0:4],fp)
        fp.close()
        client_socket.close()

if __name__ == "__main__":
    file = open("data.json","w")
    file.write("[]")
    file.close()
    server = multiprocessing.Process(target=fcs_scheduler,args=())
    display = multiprocessing.Process(target=gui,args=())
    server.start()
    display.start()