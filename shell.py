"""
Using cmd module to create an interface for the main program.
"""

import game
import cmd
from histogram import Histogram


class Shell(cmd.Cmd):

    intro = "Welcome to Two-Dice Pigs!\n" \
    "Type ? to list commands.\n"
    prompt = "(game)"

    """
    Creates a game object with default human and computer name being Ellen and Robot fella respectively
    """
    def __init__(self):
        super().__init__()
        self.game = game.Game(human_name="Ellen", computer_name="Robot fella")

    """
    Starts game
    """
    def do_start(self, arg):
        """Start a new game."""
        self.game = game.Game(human_name=self.game.human_player.name, computer_name=self.game.computer_player.name)
        print("\nStarting a new game!\n")
        self.game.start()

    def do_change(self, arg):
        new_name = input("What is your new name? ")
        self.game.human_player.set_name(new_name)
        print(f'Your name is now {new_name}. ')

    def do_roll(self, arg):
        self.game.roll_dice()
    
    def do_showhist(self, arg):
        """Display histograms for both players."""
        self.game.human_histogram.show()
        self.game.computer_histogram.show()