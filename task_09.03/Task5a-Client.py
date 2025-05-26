

import pickle
import socket
import struct
import threading
import time

from task1.Solution1 import *


def connectToServer():
    soc = socket.socket ()
    host = '127.0.0.1'
    port = 5555

    print ('Connecting to Server ... ')
    try:
        soc.connect ((host, port))
    except socket.error as e:
        print (str (e))
    print ('Connected! ')
    return soc


def getMoveFromServer(soc, game):
    # Send game board - prepend the length of data
    data = pickle.dumps (game.getBoard ())
    length = struct.pack ('!I', len (data))
    data = length + data
    soc.sendall (data)

    # Expecting next move as string (x, y)
    response = soc.recv (1024).decode ("utf-8")
    # convert string "(x, y)" to integer tuple (x,y)
    msg = response[1:5].split (",")
    return (int (msg[0]), int (msg[1]))


def loginToServer(soc):
    soc.send (b"Login|weis@nuies.com|Pa##")
    # Expecting Welcome message
    response = soc.recv (1024).decode ("utf-8")
    print ("Server: " + response)
    return response.startswith("Welcome")


class TTT_ComputerNetworkPlayer (threading.Thread):
    def __init__(self, game):
        threading.Thread.__init__ (self)
        self.game = game

    def run(self):
        soc = connectToServer ()
        if not loginToServer(soc): # login was not successful
            print ("Could not login")
            return
        while True:
            if self.game.turn == "O":  # computer plays O
                try:
                    move = getMoveFromServer (soc, game)
                    time.sleep (2)  # wait 2 seconds before making a move
                    self.game.place_on (*move)
                except BoardIsFullException:
                    pass


if __name__ == "__main__":
    game = TTTComputer ()
    player = TTT_ComputerNetworkPlayer (game)
    player.setDaemon (True)
    player.start ()
    game.mainloop ()