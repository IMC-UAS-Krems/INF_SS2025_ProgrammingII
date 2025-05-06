import socket
import time
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.connect(("localhost", 9001))

name = input("What's your name? ")
numq = input("How many questions? ")

s.sendall(f"{name} : {numq}".encode("utf-8"))

# Okay message
response = s.recv(1024).decode("utf-8")
print(response)

while response != "END":
    response = s.recv(1024).decode("utf-8")
    print(response)

    answer = input("Answer: ")
    s.send(answer.encode("utf-8"))


s.close()