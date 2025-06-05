import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8080))

while True:
    msg = input('Enter msg: ')
    s.send(msg.encode('utf-8'))
    res = s.recv(1024).decode('utf-8')
    print(res)

