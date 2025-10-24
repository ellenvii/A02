
class Histogram:
    """histogram to track round number and player's score after each round."""

    def __init__(self, player):
        """Constructor"""
        self.player = player
        self.data = []  #represents list of tuples: (round_number, score_after_round)

    def add_entry(self, round_number, score):
        """Add the current round number and player's total score after the round."""
        self.data.append((round_number, score))

    def show(self):
        """Print a simple text-based histogram."""
        title = getattr(self.player, "name", str(self.player))
        print(f"\nHistogram for {title}:")
        print("-" * 40)
        for round_num, score in self.data:
            bar = "#" * max(1, score // 5)  #one '#' per 5 pts
            print(f"Round {round_num:2}: {bar} ({score} pts)")
        print("-" * 40)
