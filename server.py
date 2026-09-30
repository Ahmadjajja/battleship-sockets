import socket
import sys
import random

if len(sys.argv) != 2:
    print("Usage: python server.py [PORT_NUMBER]")
    sys.exit()

port = int(sys.argv[1])

board = [["." for _ in range(6)] for _ in range(6)]


def place_ship(length):
    while True:
        direction = random.choice(["horizontal", "vertical"])

        if direction == "horizontal":
            row = random.randint(0, 5)
            column = random.randint(0, 6 - length)

            can_place = True

            for i in range(length):
                if board[row][column + i] == "S":
                    can_place = False

            if can_place:
                for i in range(length):
                    board[row][column + i] = "S"
                break

        else:
            row = random.randint(0, 6 - length)
            column = random.randint(0, 5)

            can_place = True

            for i in range(length):
                if board[row + i][column] == "S":
                    can_place = False

            if can_place:
                for i in range(length):
                    board[row + i][column] = "S"
                break


place_ship(4)
place_ship(3)
place_ship(2)

print("Server board:")
print("  1 2 3 4 5 6")
for i in range(6):
    print(i + 1, " ".join(board[i]))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("localhost", port))
server_socket.listen(1)

print("\nServer is listening on port", port)

connection, address = server_socket.accept()
print("Client connected from:", address)

while True:
    guess = connection.recv(1024).decode()

    if not guess:
        break

    row, column = guess.split()

    row = int(row) - 1
    column = int(column) - 1

    if board[row][column] == "S":
        result = "Hit"
        board[row][column] = "X"
    else:
        result = "Miss"

    print("Guess received:", row + 1, column + 1, "-", result)

    connection.send(result.encode())

connection.close()
server_socket.close()
