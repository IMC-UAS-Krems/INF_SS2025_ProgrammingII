import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
s.bind(("localhost", 9001))  # bind to an IP + port (note the tuple!)
s.listen()


def handleClient(client_sock, address_info):
    # first message contains name and questions
    message = client_sock.recv(4096).decode("utf-8")
    name = message.split(":").strip()[0]
    numquestions = int(message.split(":").strip()[1])
    print("Client", name, "connected. They want", numquestions, "questions")

    if numquestions < 1:
        client_sock.sendall("Need to ask for at least one question".encode("utf-8"))
        client_sock.sendall("END".encode("utf-8"))

    client_sock.sendall(f"Okay {name}, here we go.".encode("utf-8"))

    points = 0
    for i in range(numquestions):
        client_sock.sendall(f"""
        Question {i+1}:
        a) 1
        b) 2
        c) 3 
        """.encode("utf-8"))

        answer = client_sock.recv(4096).decode("utf-8")
        if answer == "b":
            points += 1

    client_sock.sendall("END".encode("utf-8"))
    client_sock.sendall(f"Okay {name}. You reached {points} points.".encode("utf-8"))

    client_sock.close()

while True:
    client_socket, address_info = s.accept()  # this waits for a client to connect
    t = threading.Thread(target=handleClient, args=(client_socket, address_info))
    t.start()
