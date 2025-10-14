"""
Using cmd module to create an interface for the main program.
"""

import game
import cmd


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
        self.game.start()

    def do_change(self, arg):
        new_name = input("What is your new name? ")
        self.game.human_player.set_name(new_name)
        print(f'Your name is now {new_name}. ')

    def do_roll(self, arg):
        self.game.roll_dice()
