"""Dice class"""
import random

class Die:
    """Shared attribute of all dice objects"""
    dice_graphics = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    #shall always have 6 sides
    def __init__(self, sides: int = 6):

        self.sides = sides 
        self.last_roll = 0

    """Rolls the die"""
    def roll(self) -> int:
        return random.randint(1, self.sides)
    
    """Returns the dice graphic for respective value"""
    def get_dice_graphics(self, roll: int) -> str:
        return self.dice_graphics[roll - 1] #cause index
