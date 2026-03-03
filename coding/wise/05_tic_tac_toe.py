"""
WISE PAIR PROGRAMMING — Problem 5: Tic-Tac-Toe

SCENARIO:
Friday hackathon at Wise. Build a 2-player Tic-Tac-Toe game.
Follow-ups: NxN board, undo move, AI opponent.
"""


class Board:
    """Represents the game board. Works for any NxN size."""

    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
        self.moves_history = []  # for undo

    def place(self, row, col, symbol):
        """Place symbol on the board. Returns True if valid move."""
        if not self._is_valid_position(row, col):
            return False
        if self.grid[row][col] != " ":
            return False

        self.grid[row][col] = symbol
        self.moves_history.append((row, col))
        return True

    def undo(self):
        """Remove last move from the board."""
        if not self.moves_history:
            return False
        row, col = self.moves_history.pop()
        self.grid[row][col] = " "
        return True

    def is_full(self):
        """Check if all positions are taken."""
        return all(self.grid[r][c] != " " for r in range(self.size) for c in range(self.size))

    def check_winner(self, symbol):
        """Check if the given symbol has won."""
        # Check rows
        for row in range(self.size):
            if all(self.grid[row][col] == symbol for col in range(self.size)):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size)):
                return True

        # Check main diagonal (top-left → bottom-right)
        if all(self.grid[i][i] == symbol for i in range(self.size)):
            return True

        # Check anti-diagonal (top-right → bottom-left)
        if all(self.grid[i][self.size - 1 - i] == symbol for i in range(self.size)):
            return True

        return False

    def display(self):
        """Print the board."""
        for i, row in enumerate(self.grid):
            print(" | ".join(row))
            if i < self.size - 1:
                print("-" * (self.size * 4 - 3))
        print()

    def _is_valid_position(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    """Controls the game flow."""

    def __init__(self, player1_name="Player 1", player2_name="Player 2", board_size=3):
        self.board = Board(size=board_size)
        self.players = [
            Player(player1_name, "X"),
            Player(player2_name, "O"),
        ]
        self.current_turn = 0  # index into self.players

    def current_player(self):
        return self.players[self.current_turn]

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn  # 0→1, 1→0

    def play_move(self, row, col):
        """Attempt to place current player's symbol. Returns status string."""
        player = self.current_player()

        if not self.board.place(row, col, player.symbol):
            return "INVALID"

        if self.board.check_winner(player.symbol):
            return "WIN"

        if self.board.is_full():
            return "DRAW"

        self.switch_turn()
        return "OK"

    def undo_move(self):
        """Undo last move and switch turn back."""
        if self.board.undo():
            self.switch_turn()
            return True
        return False


# --- TEST ---
if __name__ == "__main__":
    game = Game("Alice", "Bob")

    # Simulating a game: Alice (X) wins with top row
    moves = [
        (0, 0),  # Alice X
        (1, 0),  # Bob O
        (0, 1),  # Alice X
        (1, 1),  # Bob O
        (0, 2),  # Alice X — wins! (top row)
    ]

    for row, col in moves:
        player = game.current_player()
        result = game.play_move(row, col)
        game.board.display()

        if result == "WIN":
            print(f"{player.name} ({player.symbol}) WINS!")
            break
        elif result == "DRAW":
            print("DRAW!")
            break
