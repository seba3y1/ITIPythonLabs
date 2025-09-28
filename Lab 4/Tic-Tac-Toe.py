import random

# ---------------- Player ----------------
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            pos = int(input(f"{self.name} ({self.symbol}), enter a number (1-9): "))
            if pos >= 1 and pos <= 9:
                if board.update(pos, self.symbol):
                    break
                else:
                    print("place is already taken")
            else:
                print("number must be between 1 and 9")


class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) turn:")
        while True:
            pos = random.randint(1, 9)
            if board.update(pos, self.symbol):
                break


# ---------------- Board ----------------
class Board:
    def __init__(self):
        self.grid = [" "] * 9   # simple list for 9 places

    def display(self):
        print()
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]} ")
        print("---+---+---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]} ")
        print("---+---+---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]} ")
        print()

    def update(self, pos, symbol):
        index = pos - 1
        if self.grid[index] == " ":
            self.grid[index] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # check rows, columns, diagonals
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # cols
            [0,4,8], [2,4,6]            # diagonals
        ]
        for line in wins:
            if self.grid[line[0]] == self.grid[line[1]] == self.grid[line[2]] == symbol:
                return True
        return False

    def is_full(self):
        return " " not in self.grid


# ---------------- Game ----------------
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0  # 0 = player1, 1 = player2

    def play(self):
        self.board.display()
        while True:
            current = self.players[self.turn]
            current.make_move(self.board)
            self.board.display()

            if self.board.check_winner(current.symbol):
                print(f"{current.name} wins")
                break

            if self.board.is_full():
                print("it's a draw")
                break

            # switch turn
            self.turn = 1 - self.turn


# ---------------- Main ----------------
if __name__ == "__main__":
    print("Tic Tac Toe game")
    print("1. human vs human")
    print("2. human vs computer")
    choice = input("choose 1 or 2: ")

    if choice == "1":
        name1 = input("enter player 1 name: ")
        name2 = input("enter player 2 name: ")
        p1 = HumanPlayer(name1, "X")
        p2 = HumanPlayer(name2, "O")
    else:
        name = input("enter your name: ")
        p1 = HumanPlayer(name, "X")
        p2 = ComputerPlayer("computer", "O")

    game = Game(p1, p2)
    game.play()

