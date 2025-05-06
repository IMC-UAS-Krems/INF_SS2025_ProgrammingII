import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))

s.listen()

def handle_client(address, client_socket):
    message_from_client = client_socket.recv(1024)
    print("Received:", message_from_client)
    time.sleep(5)
    client_socket.sendall((b"Hello in return!"))
    client_socket.close()

while True:
    client_socket, address = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(address, client_socket))
    client_thread.start()
