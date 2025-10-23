from player import Player
from dice_hand import DiceHand
from histogram import Histogram

class Game:
    """ Game class """
    win_score = 100

    def __init__(self, human_name: str, computer_name: str):
        """Constructor"""
        self.winner = None
        self.loser = None

        self.human_player = Player(human_name)
        self.computer_player = Player(computer_name)

        self.players = [self.human_player, self.computer_player]
        self.turn_index = 0
        self.turn_total = 0
        self.game_over = False
        self.dice_hand = DiceHand(2)

        self.human_round = 0
        self.computer_round = 0

        self.human_histogram = Histogram(self.human_player)
        self.computer_histogram = Histogram(self.computer_player)

    @property 
    def current_player(self):
        """returns the current player"""
        return self.players[self.turn_index]
    
    def swap_turn(self):
        """Swaps player"""
        self.turn_total = 0
        self.turn_index = (self.turn_index + 1) % len(self.players)
        print(f"\n-- It is now {self.players[self.turn_index].name}'s turn --")
    
    @property
    def other_player(self):
        """Returns the other player"""
        return self.players[(self.turn_index + 1) % len(self.players)]
    
    def _record_round_end(self):
        """Record the end of the current player's round into respective player's round count in histogram."""
        if self.current_player is self.human_player:
            self.human_round += 1
            self.human_histogram.add_entry(self.human_round, self.human_player.score)
        else:
            self.computer_round += 1
            self.computer_histogram.add_entry(self.computer_round, self.computer_player.score)

    
    def roll_dice(self):
        """Rolls dice"""
        return self.dice_hand.roll() 
    
    def hold_and_check_win(self):
        """Allows player to hold and bank points"""
        self.current_player.hold(self.turn_total)
        print(f"{self.current_player.name} banks {self.turn_total}. Total = {self.current_player.score}")

        self._record_round_end()
        self.turn_total = 0

        if self.current_player.score >= self.win_score:
            print(f"\n {self.current_player.name} wins with {self.current_player.score} points!")
            self.game_over = True
        
         
    def start(self):
        """Starts a game"""
        print('Game has started!')
        print(f'Player 1: {self.human_player.name}')
        print(f'Player 2: {self.computer_player.name}')
        print(f"-- {self.current_player.name} starts --")

        while not self.game_over:
            if self.current_player is self.human_player:
                self.human_turn()
            else:
                self.computer_turn()

    def cheat(self):
        """Allows player to cheat"""
        pass
    
    def computer_turn(self):
        """Executes what happens during the computer's turn"""
        HOLD_AT = 20  # super basic strategy
        while True:
            r1, r2, total = self.roll_dice()
            if not self.handle_roll(r1, r2, total):
                return
            projected = self.current_player.score + self.turn_total
            if self.turn_total >= HOLD_AT or projected >= self.win_score:
                print(f"{self.computer_player.name} holds with {self.turn_total}.")
                self.hold_and_check_win()
                if not self.game_over:
                    self.swap_turn()
                return

    def human_turn(self):
            """Executes what happens during the human player's turn"""
            while True:
                r1, r2, total = self.roll_dice()
                if not self.handle_roll(r1,r2, total):
                     return
                hold_or_roll = input("Do you wish to hold or roll again? ")
                if hold_or_roll == "h":
                    self.hold_and_check_win()
                    if not self.game_over:
                         self.swap_turn()
                    return
    
    def handle_roll(self, r1, r2, total):
        """Game logic"""
        if r1 == 1 and r2 == 1:
            print("Bruh you scored snake eyes all ur points are gone. ")
            self.current_player.reset_score()
            self.turn_total = 0

            self._record_round_end()

            self.swap_turn()
            return False
    
        elif r1 == 1 or r2 == 1:
            print("I see a 1 — you got no points this turn.")
            self.turn_total = 0

            self._record_round_end()

            self.swap_turn()
            return False
        
        else:
            self.turn_total += total
            potential_score = self.current_player.score + self.turn_total
            print(f"Current turn total:{self.turn_total}\nPotential score: {potential_score}")
            return True
    