import player

class Highscore():
    """Keeps track of the highest scores across games."""

    def __init__(self):
        self.scores = []  # list of tuples: (name, score)

    def add_score(self, name, score):
        """Add a new score and keep only top 5."""
        self.scores.append((name, score))
        # sort by score (descending) and keep top 5
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:5]

    def show(self):
        """Display the highscores."""
        if not self.scores:
            print("\nNo highscores yet!\n")
            return
        
        print("\n🏆 Highscores 🏆")
        for i, (name, score) in enumerate(self.scores, start=1):
            print(f"{i}. {name}: {score} points")
        print()
