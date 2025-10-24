"""Dice class"""

import random


class Die:
    """Class of 1 die"""

    dice_graphics = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    """Shared attribute of all dice objects"""

    # shall always have 6 sides
    def __init__(self, sides: int = 6):
        """Constructor"""
        self.sides = sides
        self.last_roll = 0

    def roll(self) -> int:
        """Rolls the die"""
        return random.randint(1, self.sides)

    def get_dice_graphics(self, roll: int) -> str:
        """Returns the dice graphic for respective value"""
        return self.dice_graphics[roll - 1]  # cause index
