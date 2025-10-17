from player import Player
from dice_hand import DiceHand

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

    @property
    def current_player(self):
        return self.players[self.turn_index]
    
    def swap_turn(self):
        self.turn_total = 0
        self.turn_index = (self.turn_index + 1) % len(self.players)
        print(f"\n-- It is now {self.players[self.turn_index].name}'s turn --")
    
    @property
    def other_player(self):
        return self.players[(self.turn_index + 1) % len(self.players)]
    
    def roll_dice(self):
        return self.dice_hand.roll() 
    
    def hold_and_check_win(self):
        self.current_player.hold(self.turn_total)
        print(f"{self.current_player.name} banks {self.turn_total}. Total = {self.current_player.score}")
        if self.current_player.score >= self.win_score:
            print(f"\n {self.current_player.name} wins with {self.current_player.score} points!")
            self.game_over = True
         
    def start(self):
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
            pass
    
    def computer_turn(self):
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
        if r1 == 1 and r2 == 1:
            print("Bruh you scored snake eyes all ur points are gone. ")
            self.current_player.reset_score()
            self.swap_turn()
            return False

        elif r1 == 1 or r2 == 1:
             print("i see a 1, u got no points this turn. ")
             self.swap_turn()
             return False
        else:
            self.current_player.add_points(total)
            self.turn_total += total
            print(f"Current turn total:{self.turn_total}\nPotential score: {self.current_player.score + self.turn_total}")
            return True
    