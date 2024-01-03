global queue

def insert_queue(token):
    global queue
    queue.append(token)

def remove_queue():
    global queue
    return queue.pop(0)

def main():
    while True:
        