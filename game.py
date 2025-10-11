from dice import Die
from player import Player

class Game:

    win_score = 100

    def __init__(self, human_name, computer_name ):

        self.winner = None
        self.loser = None

        self.human_player = Player(human_name)
        self.computer_player = Player(computer_name)
        self.game_over = False
    
    def roll_dice(self):
        pass

    def start(self):
        pass

    def cheat(self):
        pass