from enum import Enum
from colorama import Fore, Style


class Player(Enum):
    first_player = "X"
    second_player = "O"
    empty = " "


class Board:
    BOARD_SIZE = 9
    VICTORY_SETS = [{0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 4, 8}, {2, 4, 6}]

    def __init__(self):
        self._occupied: dict[int, Player] = {}
        self.winner: Player | None = None
        self.print_iterator = self.print_board()

    def validate(self, inner_location: int):
        # check if inner_location chosen is free on the board
        return 0 <= inner_location < self.BOARD_SIZE and inner_location not in self._occupied

    def update(self, inner_location: int, sign: Player) -> None:
        # gets player's inner location selection and the player's sign
        # updates the occupied dict with player's sign
        # return chosen location
        self._occupied[inner_location] = sign

    def __getitem__(self, item):
        return self._occupied.get(item)

    @property
    def is_full(self):
        return len(self._occupied) == self.BOARD_SIZE

    def check_victory(self) -> bool:
        # check if board is won by same player
        for victory_set in self.VICTORY_SETS:
            for player in Player:
                if all([self._occupied.get(location) == player for location in victory_set]):
                    self.winner = player
                    self.print_iterator = self.print_x() if player == Player.first_player else self.print_o()
                    return True
        return False

    def print_board(self):
        while True:
            yield f" {self._occupied.get(0, Player.empty).value} ## {self._occupied.get(1, Player.empty).value} ## {self._occupied.get(2, Player.empty).value}      "
            yield f"#############     "
            yield f" {self._occupied.get(3, Player.empty).value} ## {self._occupied.get(4, Player.empty).value} ## {self._occupied.get(5, Player.empty).value}      "
            yield f"#############     "
            yield f" {self._occupied.get(6, Player.empty).value} ## {self._occupied.get(7, Player.empty).value} ## {self._occupied.get(8, Player.empty).value}      "

    @staticmethod
    def print_o():
        while True:
            yield f"     O O          "
            yield f"  O       O       "
            yield f"  O       O       "
            yield f"  O       O       "
            yield f"     O O          "

    @staticmethod
    def print_x():
        while True:
            yield f"  X       X       "
            yield f"    X   X         "
            yield f"      X           "
            yield f"    X   X         "
            yield f"  X       X       "


class Controller:
    BOARD_SIZE = 9

    def __init__(self):
        self.main_board: list[Board] = [Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board()]
        self.score = Board()
        self.turn = Player.first_player
        self.last = None

    def print_board(self):
        for big_board_row in range(3):
            for width in range(5):
                for small_board in range(3):
                    location = 3 * big_board_row + small_board
                    color = Fore.YELLOW if location == self.last else ""
                    print(color + next(self.main_board[location].print_iterator) + Style.RESET_ALL, end="")
                print()
            print('\n')

    def validate_board_choice(self, upper_location: int) -> bool:
        # fails full boards
        # fails won boards
        # allow only boards according to last move location
        return (
            0 <= upper_location < self.BOARD_SIZE and
            self.score[upper_location] is None and
            not self.main_board[upper_location].is_full
        )

    def get_user_input(self):
        if self.last is None:
            location = int(input("choose a board"))
            while not self.validate_board_choice(location):
                location = int(input("choose a valid board"))
        else:
            location = self.last
        inner_location = int(input("choose a location"))
        while not self.main_board[location].validate(inner_location):
            inner_location = int(input("choose a valid square"))
        return location, inner_location

    def move(self, location: int, inner_location: int) -> None:
        self.main_board[location].update(inner_location, self.turn)
        if not self.score[location] and self.main_board[location].check_victory():
            self.score.update(location, self.turn)
        self.last = inner_location if self.validate_board_choice(inner_location) else None
        self.turn = Player.second_player if self.turn == Player.first_player else Player.first_player

    def run(self):
        while not self.score.check_victory():
            self.print_board()
            self.move(*self.get_user_input())

        self.print_board()
        print(f"{self.score.winner.value} Won!")


def play():
    Controller().run()


if __name__ == '__main__':
    play()
