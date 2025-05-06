import socket
import time
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.connect(("localhost", 9000))

msg = f"Hi Server {randint(0,100)}".encode('utf-8')
print(f"Sending {msg}")
s.sendall(msg)

message_from_server = s.recv(4096)
print("Server replied", message_from_server)

s.close()