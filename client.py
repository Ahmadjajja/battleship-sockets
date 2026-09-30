import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python client.py [PORT_NUMBER]")
    sys.exit()

port = int(sys.argv[1])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", port))

print("Connected to server on port", port)

board = [["?" for _ in range(6)] for _ in range(6)]

guesses = 0
hits = 0

while hits < 9:
    print("\nCurrent board:")
    print("  1 2 3 4 5 6")

    for i in range(6):
        print(i + 1, " ".join(board[i]))

    try:
        row = int(input("\nEnter row (1-6): "))
        column = int(input("Enter column (1-6): "))

        if row < 1 or row > 6 or column < 1 or column > 6:
            print("Please enter numbers from 1 to 6.")
            continue

    except ValueError:
        print("Please enter valid numbers.")
        continue

    if board[row - 1][column - 1] != "?":
        print("You already guessed that square.")
        continue

    guess = str(row) + " " + str(column)

    client_socket.send(guess.encode())

    result = client_socket.recv(1024).decode()

    guesses += 1

    if result == "Hit":
        print("Hit!")
        board[row - 1][column - 1] = "X"
        hits += 1

    else:
        print("Miss!")
        board[row - 1][column - 1] = "O"

print("\nCurrent board:")
print("  1 2 3 4 5 6")

for i in range(6):
    print(i + 1, " ".join(board[i]))

print("\nYou sank all the battleships!")
print("Total guesses:", guesses)

client_socket.close()
