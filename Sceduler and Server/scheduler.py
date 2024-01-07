import socket
global queue 
queue = [1,2,3,4,5]

def insert_token(token):
    global queue
    queue.append(token)

def remove_token():
    global queue
    return queue.pop(0)

def prempt_token(token):
    global queue
    queue.append(queue.pop(queue.index(token)))

def fcs_scheduler():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 1234))
    server_socket.listen(1)
    print("Scheduler started")
    while True:
        client_socket, address = server_socket.accept()
        print("Connection from", address)
        data = client_socket.recv(1024)
        data = data.decode()
        if data == "next_token":
            token = remove_token()
            client_socket.send(bytes(token, "utf-8"))
        elif data == "hold_token":
            token = client_socket.recv(1024)
            token = token.decode()
            prempt_token(token)
        elif data == "insert_token":
            token = client_socket.recv(1024)
            token = token.decode()
            insert_token(token)
        print(queue)
        client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    fcs_scheduler()

