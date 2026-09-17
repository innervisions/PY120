class Game:
    def play(self):
        return "Start the game!"


class Bingo(Game):
    pass

game_of_bingo = Bingo()
print(game_of_bingo.play())  # 'Start the game!'
