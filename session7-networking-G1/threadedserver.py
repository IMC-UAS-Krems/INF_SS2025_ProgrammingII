import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.bind(("localhost", 9000))  # bind to an IP + port (note the tuple!)
s.listen()

def handleClient(client_sock, address_info):
    print("A client from address ", address_info, "just connected")

    message = client_sock.recv(4096)  # listen to the client
    print("Client said", message)

    time.sleep(5)

    client_sock.sendall("Delayed hi from the Server!".encode("utf-8"))
    client_sock.close()

while True:
    client_socket, address_info = s.accept()  # this waits for a client to connect
    t = threading.Thread(target=handleClient, args=(client_socket, address_info))
    t.start()

# message = client_socket.recv(4096)  # listen to the client
# print("Client said", message)
#
# client_socket.sendall("Hi from the Server!".encode("utf-8"))
# client_socket.close()

# s.close()