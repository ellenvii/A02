from player import Player
from dice import Die

class Game:
    win_score = 100

    def __init__(self, human_name: str, computer_name: str):
        self.winner = None
        self.loser = None

        self.human_player = Player(human_name)
        self.computer_player = Player(computer_name)

        self.game_over = False

        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        r1 = self.die1.roll()
        r2 = self.die2.roll()
        g1 = self.die1.get_dice_graphics(r1)
        g2 = self.die2.get_dice_graphics(r2)
        total = r1 + r2
        print(f'You rolled {g1} {g2} ({r1}+{r2}={total})! ')
        return r1, r2, total

    def start(self):
        print('Game has started!')
        print(f'Player 1: {self.human_player.name}')
        print(f'Player 2: {self.computer_player.name}')

    def cheat(self):
        pass
