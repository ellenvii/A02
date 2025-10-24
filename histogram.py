from __future__ import annotations
from typing import List, Tuple, Any

class Histogram:
    """histogram to track round number and player's score after each round."""

    def __init__(self, player: Any) -> None:
        """Constructor"""
        self.player = player
        self._sessions: List[List[Tuple[int, int]]] = [[]]  # list of games
        self.data: List[Tuple[int, int]] = self._sessions[-1]

    def set_player(self, player: Any) -> None:
        """Update the player reference (useful if reusing one histogram across new Game instances)."""
        self.player = player

    def start_new_game(self) -> None:
        """Begin a new game session; subsequent add_entry calls go to this session."""
        self._sessions.append([])
        self.data = self._sessions[-1]

    def add_entry(self, round_number: int, score: int) -> None:
        """Add the current round and player's total score after the round to the current session."""
        self.data.append((round_number, score))

    def show(self) -> None:
        """Print a simple text-based histogram for each game session."""
        title = getattr(self.player, "name", str(self.player))
        print(f"\nHistogram for {title}:")
        for idx, session in enumerate(self._sessions, start=1):
            print("-" * 40)
            if len(self._sessions) > 1:
                print(f"Game {idx}")
            for round_num, score in session:
                bar = "#" * max(1, score // 5)  # one '#' per 5 pts
                print(f"Round {round_num:2}: {bar} ({score} pts)")
        print("-" * 40)
