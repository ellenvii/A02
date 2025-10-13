"""
Player class
"""

class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name): # initialize a new player with given name, it was for a small test checking on pytest
        self.name = name
        self.score = 0 # player starts with 0 points
    
    def add_points(self, points):
        if points < 0:
            raise ValueError("Can't add negative points.")
        else:
            self.score += points
    
    def set_name(self, new_name):
        self.name = new_name
    
    def reset_score(self):
        self.score = 0
    

