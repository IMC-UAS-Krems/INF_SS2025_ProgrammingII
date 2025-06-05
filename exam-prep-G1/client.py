import socket

HOST = '127.0.0.1'  # The server's address
PORT = 65432        # The server's port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to server.")

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print("Server echoed:", data.decode())