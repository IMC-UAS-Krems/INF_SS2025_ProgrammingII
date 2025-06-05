import socket

HOST = '127.0.0.1'  # localhost
PORT = 65432        # non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Server is listening on", HOST, PORT)
    conn, addr = server_socket.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received from client:", data.decode())
            conn.sendall(data)  # Echo back