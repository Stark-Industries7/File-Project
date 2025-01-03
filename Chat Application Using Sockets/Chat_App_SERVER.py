# import socket
# import time
# import threading

# HEADER = 1024
# PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER,PORT)
# FORMAT = 'utf-8'
# DISCONNECT_MSG = '!DISCONNECT'

# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(ADDR)

# clients = {}

# def handle_client(conn,addr):
#     print(f"[NEW CONNECTION] : New Connection {addr} Connected!")
    
#     # Receive username
#     username = conn.recv(HEADER).decode(FORMAT)
#     clients[conn] = username
#     print(f"[USERNAME SET] {username} has joined the chat!")
    
#     connected = True
#     while connected:
#         msg_len = conn.recv(HEADER).decode(FORMAT)
#         if msg_len:
#             msg_len = int(msg_len)
#             msg = conn.recv(msg_len).decode(FORMAT)
#             if msg == DISCONNECT_MSG:
#                 connected = False
#             print(f"[{addr}] : Message [{msg}]")
#             conn.send("Message Received!".encode(FORMAT))
#     conn.close()
#     del clients[conn]            


# def start():
#     server.listen()
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client,args=(conn,addr))
#         thread.start()
#         print(f"[ACTIVE CONNECTION] : {threading.active_count() - 1}")
#         if (threading.active_count() - 1) == 0:
#             print(f"[ACTIVE CONNECTION] : No Active Connections!")


# print("[SERVER] : Starting Server........")
# print(f"[SERVER] : Server listening at IP Address :: [{SERVER}]")
# time.sleep(5)
# start()


import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = {}  # Store client connections and usernames

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    # Receive and set the username as the first message
    username_length = conn.recv(HEADER).decode(FORMAT)
    username_length = int(username_length.strip())
    username = conn.recv(username_length).decode(FORMAT)
    clients[conn] = username
    print(f"[USERNAME SET] {username} has joined the chat!")

    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len.strip())
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            else:
                print(f"[{username}] {msg}")
                broadcast_message(f"{username}: {msg}", conn)
    conn.close()
    del clients[conn]

def broadcast_message(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.send(message.encode(FORMAT))

def start():
    server.listen()
    print(f"[SERVER STARTED] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[SERVER] Starting...")
start()

