import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Card:
    SUITS = ("♤", "♧", "♡", "♢")
    RANKS = tuple([str(num) for num in range(2, 10)] + ["A", "J", "Q", "K"])
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._hidden = False
        
    def __str__(self):
        if self._hidden:
            return "??"
        else:
            return f"{self.suit} {self.rank}"
    
    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if value not in Card.RANKS:
            raise ValueError(f"Invalid rank: {value}")
        self._rank = value
    
    @property
    def suit(self):
        return self._suit   
    
    @suit.setter
    def suit(self, value):
        if value not in Card.SUITS:
            raise ValueError(f"Invalid suit: {value}")
        self._suit = value
    
    @property
    def points(self):
        if self.rank == "A":
            return 11
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return int(self.rank)
        
    def hide(self):
        self._hidden = True
    
    def reveal(self):
        self._hidden = False


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
    
    def deal_face_down(self):
        card = self.deal()
        card.hide()
        return card

class Hand:
    def __init__(self):
        self.cards = []
        
    def reset(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def total(self):
        total_points = sum(card.points for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "A")
        while total_points > TwentyOneGame.TARGET_SCORE and aces:
            total_points -= 10
            aces -= 1
        return total_points
    
    def is_busted(self):
        return self.total() > TwentyOneGame.TARGET_SCORE
    
    def display(self):
        return ", ".join(str(card) for card in self.cards)
    
    def display_with_total(self):
        return f"{self.display()} (Total: {self.total()})"    

class Player:
    INITIAL_CASH = 5
    WINNING_CASH = 2 * INITIAL_CASH
    def __init__(self):
       self.hand = Hand()
       self.cash = self.INITIAL_CASH

    def win_bet(self):
        self.cash += 1
    
    def lose_bet(self):
        self.cash -= 1
        
    def is_broke(self):
        return self.cash <= 0
    
    def is_rich(self):
        return self.cash >= self.WINNING_CASH
    
    def show_winnings(self):
        print(f"You have ${self.cash}.")

class Dealer:
    def __init__(self):
        self.hand = Hand()

class TwentyOneGame:
    TARGET_SCORE = 21
    DEALER_STANDS = 17

    def __init__(self):
        self.deck = None
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()
        while not self.is_game_over():
            self.play_round()
            self.show_results()
            self.next_round_prompt()
            clear_screen()
        self.display_game_over_message()
        self.display_goodbye_message()

    def deal_cards(self):
        self.deck = Deck()
        self.player.hand.reset()
        self.dealer.hand.reset()
        self.player.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal_face_down())
        self.dealer.hand.add_card(self.deck.deal())

    def show_cards(self):
        print("Dealer's cards:")
        print(self.dealer.hand.display())
        print("Your cards:")
        print(self.player.hand.display_with_total())

    def player_turn(self):
        while True:
            choice = input("Do you want to hit or stay? (h/s): ").strip().lower()
            if choice == "h":
                self.player.hand.add_card(self.deck.deal())
                print("Your cards:")
                print(self.player.hand.display_with_total())
                if self.player.hand.is_busted():
                    break
            elif choice == "s":
                break
            else:
                print("Invalid choice. Please enter 'h' to hit or 's' to stay.")

    def dealer_turn(self):
        self.dealer.hand.cards[0].reveal()
        print("Dealer's cards:")
        print(self.dealer.hand.display_with_total())
        while self.dealer.hand.total() < self.DEALER_STANDS:
            self.dealer.hand.add_card(self.deck.deal())
            print("Dealer hits.")
            print("Dealer's cards:")
            print(self.dealer.hand.display_with_total())
            if self.dealer.hand.is_busted():
                return
        print("Dealer stays.")

    def show_results(self):
        if self.player.hand.is_busted():
            print("You went bust. Dealer wins.")
            self.player.lose_bet()
        elif self.dealer.hand.is_busted():
            print("Dealer busts! You win!")
            self.player.win_bet()
        else:
            player_total = self.player.hand.total()
            dealer_total = self.dealer.hand.total()
            print(f"Your total: {player_total}, Dealer's total: {dealer_total}")
            if player_total > dealer_total:
                print("You win!")
                self.player.win_bet()
            elif player_total < dealer_total:
                print("Dealer wins.")
                self.player.lose_bet()
            else:
                print("It's a push.")
            
    def play_round(self):
        self.player.show_winnings()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        if not self.player.hand.is_busted():
            self.dealer_turn()
            
    def next_round_prompt(self):
        input("Press Enter to continue to the next round...")

    def display_welcome_message(self):
        print("Welcome to Twenty-One!")

    def display_goodbye_message(self):
        print("Thank you for playing Twenty-One!")

    def is_game_over(self):
        return self.player.is_broke() or self.player.is_rich()

    def display_game_over_message(self):
        self.player.show_winnings()
        if self.player.is_broke():
            print("You went broke! Game over.")
        elif self.player.is_rich():
            print("You have doubled your money! You win!")


game = TwentyOneGame()
game.start()
