import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen()
client_socket, address = s.accept()

while True:
    msg = client_socket.recv(1024).decode()
    print(msg)
    client_socket.sendall(msg.encode('utf-8'))

