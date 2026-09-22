import random
import os


def clear_screen():
    os.system("clear")


class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER


class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {idx: Square() for idx in range(1, 10)}

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display(self):
        print()
        print("     |     |")
        print(
            f"  {self.squares[1]}  |"
            f"  {self.squares[2]}  |"
            f"  {self.squares[3]}"
        )
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(
            f"  {self.squares[4]}  |"
            f"  {self.squares[5]}  |"
            f"  {self.squares[6]}"
        )
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(
            f"  {self.squares[7]}  |"
            f"  {self.squares[8]}  |"
            f"  {self.squares[9]}"
        )
        print("     |     |")
        print()

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()


class Player:

    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)
        
    def __str__(self):
        return "You"


class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

    def __str__(self):
        return "Computer"


class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    MATCH_WINS = 3

    @staticmethod
    def join_or(lst, delimiter=', ', conjunction='or'):
        match len(lst):
            case 0:
                return ""
            case 1:
                return lst[0]
            case 2:
                return f'{lst[0]} {conjunction} {lst[1]}'
        beginning = delimiter.join(str(el) for el in lst[0:-1])
        return f'{beginning}{delimiter}{conjunction} {lst[-1]}'

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        clear_screen()
        self.display_scores()
        self.display_welcome_message()
        self.board.display()
        self.play_match()
        self.display_goodbye_message()

    def play_match(self):
        first_player = random.choice([self.human, self.computer])
        while not self.match_winner():
            self.play_round(first_player)
            if self.match_winner():
                break
            if self.play_again():
                self.board.reset()
                first_player = self.swap_players(first_player)
                self.display_scores()
                self.board.display()
            else:
                return
        self.display_match_winner()

    def match_winner(self):
        if self.human.score >= self.MATCH_WINS:
            return self.human
        if self.computer.score >= self.MATCH_WINS:
            return self.computer

        return None

    def display_match_winner(self):
        print(f"\nYou won {self.human.score}.")
        print(f"Computer won {self.computer.score}.")
        print(f"{self.match_winner()} wins the match.")

    def play_round(self, first_player):
        second_player = self.swap_players(first_player)
        while True:
            self.player_moves(first_player)
            if self.is_game_over():
                break

            self.display_scores()
            self.board.display()

            self.player_moves(second_player)
            if self.is_game_over():
                break
            self.display_scores()
            self.board.display()

        self.display_scores()
        self.board.display()
        self.display_results()

    def play_again(self):
        while True:
            again = input("Would you like to play again? (y/n): ").lower()
            if again not in ("y", "n"):
                print("Please choose y or n.")
                continue
            break

        return again == 'y'

    def swap_players(self, player):
        return self.human if player == self.computer else self.computer

    def player_moves(self, player):
        if player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_scores(self):
        clear_screen()
        print("*" * 35)
        print(f"Player: {self.human.score}    |    "
              f"Computer: {self.computer.score}")
        print(f'Win {TTTGame.MATCH_WINS} rounds to win the match!')
        print("*" * 35)

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
            self.human.score += 1
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
            self.computer.score += 1
        else:
            print("A tie game. How boring.")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def human_moves(self):
        valid_choices = self.board.unused_squares()

        while True:
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame.join_or(choices_list, ", ", "or")
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()
        if not choice:
            choice = self.defensive_computer_move()
        if not choice:
            choice = self.pick_center_square()
        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)

    def defensive_computer_move(self):
        return self.find_crtical_square(self.human)

    def offensive_computer_move(self):
        return self.find_crtical_square(self.computer)

    def pick_center_square(self):
        return 5 if self.board.squares[5].is_unused() else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def find_crtical_square(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key

        return None

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.squares[key].is_unused():
                    return key

        return None

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return self.is_winner(self.human) or self.is_winner(self.computer)


game = TTTGame()
game.play()
