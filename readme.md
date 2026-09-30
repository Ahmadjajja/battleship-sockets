Video Demo: https://youtu.be/uDWJ33D2qtI?si=U0Y_iZJpVqaKbAO0

# Programming Assignment 1 - Battleship with Sockets

## Name
Prakriti Baral, Ahmad Sultan 

## How to Run

Open two Terminal windows or tabs.

In the first Terminal, go to the PA1 folder and run:

python3 server.py 5001

In the second Terminal, go to the same PA1 folder and run:

python3 client.py 5001

The client will display a 6x6 board and ask for a row and column number from 1 to 6.

The symbols on the client board mean:

- ? = Not guessed yet
- X = Hit
- O = Miss

The game continues until all battleship spaces are hit.

At the end, the client displays the total number of guesses used to win.

## Files

- server.py - Creates the battleship board, listens for the client, checks guesses, and sends Hit or Miss responses.
- client.py - Connects to the server, sends guesses, displays the current board, and keeps track of the game.
