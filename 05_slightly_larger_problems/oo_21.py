import random

class Card:
    SUITS = ("♤", "♧", "♡", "♢")
    RANKS = tuple([str(num) for num in range(2, 10)] + ["A", "J", "Q", "K"])
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._hidden = False
    
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
        return ", ".join(f"{card.suit}{card.rank}" for card in self.cards)    

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
        return f"You have ${self.cash}."

class Dealer:
    def __init__(self):
        self.hand = Hand()

class TwentyOneGame:
    TARGET_SCORE = 21
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        pass

    def start(self):
        # SPIKE
        self.display_welcome_message()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        # STUB
        pass

    def show_cards(self):
        # STUB
        pass

    def player_turn(self):
        # STUB
        pass

    def dealer_turn(self):
        # STUB
        pass

    def display_welcome_message(self):
        # STUB
        pass

    def display_goodbye_message(self):
        # STUB
        pass

    def display_result(self):
        # STUB
        pass

game = TwentyOneGame()
game.start()
