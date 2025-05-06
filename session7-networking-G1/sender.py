import socket

# Connecting to a local server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9000))

while True:
    inp = input("Type something:")
    if inp == "bye":
        break
    s.sendall(inp.encode("utf-8"))
    msg = s.recv(4096)
    msg = msg.decode("utf-8")
    print("Got this message from server", msg)

s.close()

