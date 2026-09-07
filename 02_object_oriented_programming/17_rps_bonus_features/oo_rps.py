import random

class Move:
    def __eq__(self, other):
        type(self) == type(other)

class Rock(Move):
    def __str__(self):
        return "rock"
    
    def __gt__(self, other):
        return isinstance(other, Scissors) or isinstance(other, Lizard)

class Paper(Move):
    def __str__(self):
            return "paper"
    
    def __gt__(self, other):
            return isinstance(other, Rock) or isinstance(other, Spock)

class Scissors(Move):
    def __str__(self):
            return "scissors"
        
    def __gt__(self, other):
            return isinstance(other, Paper) or isinstance(other, Lizard)

class Lizard(Move):
    def __str__(self):
            return "lizard"
        
    def __gt__(self, other):
            return isinstance(other, Paper) or isinstance(other, Spock)

class Spock(Move):
    def __str__(self):
            return "spock"
    def __gt__(self, other):
            return isinstance(other, Rock) or isinstance(other, Scissors)

class Player:
    CHOICES = {"rock": Rock, "paper": Paper, "scissors": Scissors, "lizard": Lizard, "spock": Spock}

    def __init__(self):
        self.move = None
        self.score = 0


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choices = list(Player.CHOICES.values())
        self.move = random.choice(choices)()


class Human(Player):
    @staticmethod
    def process_choice(player_choice):
        player_choice = player_choice.lower()
        if player_choice.startswith("r"):
            return "rock"
        if player_choice.startswith("p"):
            return "paper"
        if player_choice.startswith("sc"):
            return "scissors"
        if player_choice.startswith("l"):
            return "lizard"
        if player_choice.startswith("sp"):
            return "spock"
        
        return ""
    
    @staticmethod
    def join_or(words):
        return ", ".join(words[:-1]) + ", or " + words[-1]
    
    def __init__(self):
        super().__init__()

    def choose(self):
        choices = list(Player.CHOICES.keys())
        prompt = f"Please choose {Human.join_or(choices)}: "

        while True:
            choice = input(prompt).lower()
            choice = Human.process_choice(choice)
            if choice in Player.CHOICES:
                break

            print(f"Sorry, that is not a valid choice.")

        self.move = Player.CHOICES[choice]()


class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        
    def _reset_scores(self):
        self._human.score = 0
        self._computer.score = 0

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors. Goodbye!")
        
    def _display_header(self):
        print("-" * 55)
        print(
            f"|        Player: {self._human.score}        |"
            + f"        Computer: {self._computer.score}        |"
        )
        print("-" * 55)

    def _human_wins(self):
        return self._human.move > self._computer.move

    def _computer_wins(self):
        self._computer.move > self._human.move

    def _determine_round_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            self._human.score += 1
        elif self._computer_wins():
            print('Computer wins!')
            self._computer.score += 1
        else:
            print("It's a tie")
            
    def _display_match_winner(self):
        self._display_header()
        print(f"You won {self._human.score}.")
        print(f"Computer won {self._computer.score}.")
        if self._human.score > self._computer.score:
            print("You win the match!")
        else:
            print("Computer wins the match.")
            
    def _play_round(self):
        self._display_header()
        self._human.choose()
        self._computer.choose()
        self._determine_round_winner()

    def play(self):
        self._display_welcome_message()
        while True:
            while max((self._human.score, self._computer.score)) < 5:
                self._play_round()
            self._display_match_winner()
            if not self._play_again():
                break
            self._reset_scrores()

        self._display_goodbye_message()

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

RPSGame().play()
