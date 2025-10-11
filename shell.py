"""
Using cmd module to create an interface for the main program.
"""

import game
import cmd


class Shell(cmd.Cmd):

    intro = "Welcome to Two-Dice Pigs!" \
    "Type ? to list commands."
    prompt = "(game)"

    print(intro)


