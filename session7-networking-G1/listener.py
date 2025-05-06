import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5050))
s.listen()
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    formatRequested = data.decode("utf-8")
    print(formatRequested)
    if not data: # end of data = ''
        break
    # conn.sendall(datetime.datetime.now().strftime(formatRequested).encode("utf-8"))
conn.close()

# s.close()
