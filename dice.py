"""
Dice class
"""
import random

class Die:
    """
    Constructor - shall always have 6 sides
    """
    def __init__(self, sides: int = 6):
        self.sides = sides
    
    def roll(self) -> int:
        return random.randint(1, self.sides)
