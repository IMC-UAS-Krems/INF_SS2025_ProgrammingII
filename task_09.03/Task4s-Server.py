import socket
import _thread
import pickle
import random
import struct
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5555

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen()


# sorry, no intelligence around here ;-)
def calculateNextMove(board):
    possible = []  # collect all possible moves
    for x in range (3):
        for y in range (3):
            # nothing placed on this position yet
            if len (board[x][y]) == 0:
                possible.append ((x, y))
    if len (possible) > 0:
        # randomly select one possible move
        return random.choice (possible)
    return None

def handle_client(client_socket):
    while True:
        # read the length info.
        buf = b''
        while len (buf) < 4:
            buf += client_socket.recv (4 - len (buf))
        length = struct.unpack ('!I', buf)[0]

        data = client_socket.recv(length)
        board = pickle.loads(data)
        print ("GOT:", board)
        move = calculateNextMove(board)
        reply = str(move)
        client_socket.sendall(str.encode(reply))

    #client_socket.close()

while True:
    client_socket, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    _thread.start_new_thread(handle_client, (client_socket, ))

ServerSocket.close()