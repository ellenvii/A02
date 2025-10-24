"""
Using cmd module to create an interface for the main program.
"""

import game
import cmd
from histogram import Histogram
from highscore import Highscore

class Shell(cmd.Cmd):

    highscore = Highscore()
    intro = "Welcome to Two-Dice Pigs!\nType ? to list commands.\n"
    prompt = "(game)"

    """
    Creates a game object with default human and computer name being You and Robot fella respectively
    """
    def __init__(self):
        super().__init__()
        self.game = game.Game(human_name="You", computer_name="Robot fella", highscore = self.highscore)

    def do_start(self, arg):
        """Start a new game."""
        self.game = game.Game(human_name=self.game.human_player.name, 
                              computer_name=self.game.computer_player.name,
                              highscore = self.highscore
                              )
        print("\nStarting a new game!\n")
        self.game.start()

    def do_change(self, arg):
        """Changes player name"""
        print(f"Your current name: {self.game.human_player.name}\n"
        f"Computer's current name: {self.game.computer_player.name}\n")
        new_name = input("What is your new name? ")
        self.game.human_player.set_name(new_name)
        print(f'Your name is now {new_name}. ')
    
    def do_showhist(self, arg):
        """Display histograms for both players."""
        self.game.human_histogram.show()
        self.game.computer_histogram.show()

    def do_highscore(self, arg):
        """Show highscores."""
        self.highscore.show()
    
    def do_difficulty(self, arg):
        """Set computer AI difficulty: easy, normal, or hard."""
        level = arg.strip().lower()
        if level not in ["easy", "normal", "hard"]:
            print("Invalid difficulty. Choose: easy, normal, or hard.")
            return
        self.game.computer_ai.difficulty = level
        print(f"Computer difficulty set to: {level}")

