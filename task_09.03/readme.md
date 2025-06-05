# Programming II Exercises 

Given is a module [TicTacToe](TicTacToe.py) which contains a class TTT. This is a fully functional game of TicTacToe. You can play against yourself (or another person).
We want to create new version of this game, so that we can play against the computer. Try running the program and playing! Its fun. 

### Task 1: TTTComputer Move Calculator
Define a subclass of "TTT" called "TTTComputer" where,
1) A new method calculateNextMove() analyses the current situation of the game and returns a tuple (x,y) representing the next possible move for the computer. You can get the current status of the board through the method getBoard() in TTT.
2) If no more moves are possible because the board is full, then raise a BoardIsFullException!

__Hints__
1) Before trying to make your algorithm smart - try to generate a list of all legal moves and return a random legal move.
2) Write test cases using Pytest to test your implementation thoroughly. Can you come up with test cases other than the ones in [Test_TTTComputer.py](Test_TTTComputer.py)?
3) NO CHANGES are allowed in the file [TicTacToe.py](TicTacToe.py)

### Task 2: TTTComputer Player
We want to play TicTacToe against the computer, so we need a computer player. This is simulated by a background thread that makes the move on behalf of the computer:
1) To simulate the computer player, create a class `TTT_ComputerPlayer` which is a subclass of `threading.Thread`.
2) Provide the game (instance of `TTTComputer`) as input to this thread
3) The thread should wait, until its turn (computer plays "O"), see `TTT.turn`
4) When its the turn of the computer, it calculates the next possible move, see _Task 1_
5) And makes the move on the game, see `TTT.place_on(x,y)`

__Hints__
0) NO CHANGES are allowed in the file [TicTacToe.py](TicTacToe.py)
1) Unpack the value returned by `calculateNextMove()` before passing it on to `place_on()`
2) For a better user experience, let the thread sleep for a few seconds before making the move
3) Here is the code to start the game against the computer
```python 
    game = TTTComputer ()
    player = TTT_ComputerPlayer(game)
    player.setDaemon(True)
    player.start()
    game.mainloop()
```

### Task 3: Let two threads play against each other

Now that you have a thread simulating a computer player, why don't you just create two threads and let the computer play against itself :-)
Now sit back and watch!

Adjust your implementation of `TTT_ComputerPlayer`, so that you can pass the symbol "X" or "O" to the thread, so that it knows when to play.
Create a class `TTT_MultiComputerPlayer` by copying/adapting `TTT_ComputerPlayer` or by subclassing it. time.sleep (0.5)  Wait 0.5 seconds before making a move, otherwise, its not so much fun to watch. 

Here is the code to start the game "computer against the computer"
```python 
   game = TTTComputer ()
   player1 = TTT_MultiComputerPlayer (game, "X")
   player1.setDaemon (True)
   player1.start ()
   player2 = TTT_MultiComputerPlayer (game, "O")
   player2.setDaemon (True)
   player2.start ()
   game.mainloop ()
```

### Task4: Remote Computer Player
We want to play Tictactoe against a computer over the internet. Adapt your solution from task2, so that the computer player thread
does not calculate its moves itself - rather contacts a server which provides the next move. The thread then simply makes the move received
from the server.

__The server is given!__

The client sends the game board: game.getBoard() to the server in every request! Use the pickle module to serialize and deserialize the board. The server expects the data such that the length of the data is prefixed
to the data about the board ! To send the data use the module struct as follows:
```python 
    data = pickle.dumps (game.getBoard ())
    length = struct.pack ('!I', len (data)) # big-endian Integer
    data = length + data
    soc.sendall (data)
```

Use port 5555 to connect to the server running on localhost. The server is provided for you: [Task4a-Server.py](Task4a-Server.py)Task4a-Server.py -> just run it!
Here is how you start the game: 
```python 
    game = TTT ()
    player = TTT_ComputerNetworkPlayer (game)
    player.setDaemon (True)
    player.start ()
    game.mainloop ()
```

### Task 5 Database on the server side
Now that we have a server that can play Tictactoe, lets extend the server from [Task4a-Server.py](Task4a-Server.py), so that it stores information in a SQLite DB.

__This time, the client is given!__ See [Task5a-Client.py](Task5a-Client.py)

The DB contains two tables: games and users - which are created using SQL statements given in [SetupDB.py](SetupDB.py)

The client logs into the server by providing a email address and a password. 
Format of the message: `"Login|email@example.com|password"`
Passwords should not saved as plain text in the DB - use PasswordUtil.py to check if the password is correct.

Registration of the user is done manually - See [SetupDB.py](SetupDB.py)

After a successful login, Server replies with `"Welcome [username]"`
Then the game starts as in Task4.

The server stores information about each game played by the user in DB. Use the table "games" for this purpose.

### Task 6 Let the fun begin! 
Combine all the code from tasks 1-5 to create a full fledged multi-player Tictactoe as your Hobby Project
_(Solution is not provided)_.

__SOME possible features:__
1) The user can choose to play local/remote and against a human or a machine
2) The engine is intelligent and poses a real challenge for a human player
3) Users can register to play with the server
4) Users can play against each other
5) Server maintains rankings of the user - users get or lose points based on the game result
6) ... 
