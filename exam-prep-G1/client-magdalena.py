import socket

HOST = '127.0.0.1'
PORT = 65432  # Must match server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server.")
    while True:
        message = input("You: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print("Server echoed:", data.decode())
