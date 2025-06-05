import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9000))

try:
    while True:
        message = input("Message to send: ")
        s.send(message.encode("utf-8"))
        msg_from_server = s.recv(4096)
        print(str(msg_from_server, 'utf-8'))
except KeyboardInterrupt:
    s.close()
    print("\nClient shutting down.")