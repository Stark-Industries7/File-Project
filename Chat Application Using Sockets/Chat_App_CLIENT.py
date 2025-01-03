# import socket
# import time

# HEADER = 1024
# SERVER = "192.168.1.31"
# PORT = 5050
# FORMAT = 'utf-8'
# DISCONNECT_MSG = "!DISCONNECT"
# ADDR = (SERVER,PORT)


# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(ADDR)


# def send_message(msg):
#     message = msg.encode(FORMAT)
#     msg_length = len(message)
#     send_length = str(msg_length).encode(FORMAT)
#     send_length += b' ' * (HEADER - len(send_length))
#     client.send(send_length)
#     client.send(message)
#     print(client.recv(2048).decode(FORMAT))


# def main():

#     print("Welcome to the Chat App By Appu!")
#     while True:
#         message = input("Enter Message (or type disconnect to Disconnect) : ")
#         if message.strip().lower() == "disconnect":
#             print("Disconnecting!")
#             time.sleep(4)
#             send_message(DISCONNECT_MSG)
#             break
#         send_message(message)  

# # send_message("Accha Mummy Kaisi Hai!")
# # send_message(DISCONNECT_MSG)


# if __name__ == "__main__":
#     main()



import socket
import threading

HEADER = 1024
SERVER = "192.168.1.7"
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive_messages():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            print(message)
        except:
            print("Connection closed.")
            break

def main():
    # Prompt for username and send it first
    username = input("Enter your username: ")
    send_message(username)  # Send username as the first message

    # Start thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == "disconnect":
            send_message(DISCONNECT_MSG)
            break
        send_message(message)

if __name__ == "__main__":
    main()
