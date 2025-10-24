"""Player class"""


class Player:
    """Represents a player in the game."""

    def __init__(
        self, name
    ):  # initialize a new player with given name, it was for a small test checking on pytest
        self.name = name
        self.score = 0  # player starts with 0 points

    def add_points(self, points):
        """Adds points to total score"""
        if points < 0:
            raise ValueError("Can't add negative points.")
        else:
            self.score += points

    def set_name(self, new_name):
        """Changes name of the player"""
        self.name = new_name

    def reset_score(self):
        """Resets the players score to 0"""
        self.score = 0

    def hold(self, points):
        """Adds points to total score"""  # redundant atm
        self.add_points(points)
