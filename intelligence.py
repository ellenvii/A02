import random

class Intelligence:
    def __init__(self, player, difficulty="normal"):
        """User's choice will determine intelligence"""
        self.player = player
        self.difficulty = difficulty.lower()

    def decide(self, turn_total, potential_score, win_score):
        """
        Return True if the computer holdsa and False if it will roll again.

        turn_total: Current accumulated turn points.
        potential_score: Player's potential score if they hold.
        win_score: Score needed to win the game.
        """
        # Always hold if the potential score would win the game
        if potential_score >= win_score:
            return True

        #difficulty levels set by roll thrersholds
        if self.difficulty == "easy":
            hold_at = 10 + random.randint(-3, 3)
        elif self.difficulty == "hard":
            hold_at = 25 + random.randint(-2, 2)
        else:  #normal
            hold_at = 18 + random.randint(-2, 2)

        if self.player.score < 50: #takes more risks
            hold_at += 2

        return turn_total >= hold_at

    def __str__(self):
        return f"Computer AI ({self.difficulty.title()})"