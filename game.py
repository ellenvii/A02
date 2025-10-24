from __future__ import annotations
from typing import Optional, Tuple
from player import Player
from dice_hand import DiceHand
from histogram import Histogram
from highscore import Highscore
from intelligence import Intelligence

class Game:
    """Game class"""
    win_score = 100

    # widths for prettier alignment
    _NAME_W = 16
    _NUM_W = 4

    def __init__(
        self,
        human_name: str,
        computer_name: str,
        highscore: Optional[Highscore] = None,
        human_histogram: Optional[Histogram] = None,
        computer_histogram: Optional[Histogram] = None,
    ) -> None:
        """Constructor"""
        self.winner = None
        self.loser = None

        self.human_player = Player(human_name)
        self.computer_player = Player(computer_name)

        self.players = [self.human_player, self.computer_player]
        self.turn_index = 0
        self.turn_total = 0
        self.game_over = False
        self.dice_hand = DiceHand(2)

        self.human_round = 0
        self.computer_round = 0

        # reuse histograms if provided
        if human_histogram is None:
            self.human_histogram = Histogram(self.human_player)
        else:
            human_histogram.set_player(self.human_player)
            self.human_histogram = human_histogram

        if computer_histogram is None:
            self.computer_histogram = Histogram(self.computer_player)
        else:
            computer_histogram.set_player(self.computer_player)
            self.computer_histogram = computer_histogram

        self.highscore = highscore
        self.computer_ai = Intelligence(self.computer_player, difficulty="normal")

    @property
    def current_player(self) -> Player:
        """Return the player whose turn it is. """
        return self.players[self.turn_index]

    @property
    def other_player(self) -> Player:
        """Return the non-active player."""
        return self.players[(self.turn_index + 1) % len(self.players)]
    
    def swap_turn(self) -> None:
        """Swap to the other player and reset the turn total."""
        self.turn_total = 0
        self.turn_index = (self.turn_index + 1) % len(self.players)
        print(f"\n➡️  It is now {self.current_player.name}'s turn")

    def _record_round_end(self) -> None:
        """Record the end of the active player's round in their histogram."""
        if self.current_player is self.human_player:
            self.human_round += 1
            self.human_histogram.add_entry(self.human_round, self.human_player.score)
        else:
            self.computer_round += 1
            self.computer_histogram.add_entry(
                self.computer_round, self.computer_player.score
            )

    def roll_dice(self) -> Tuple[int, int, int]:
        """Roll both dice and return (r1, r2, total)."""
        return self.dice_hand.roll()

    def hold_and_check_win(self) -> None:
        """Bank the turn total for the current player and check for a win."""
        self.current_player.hold(self.turn_total)
        # 💰 bank line with neat columns
        print(
            f"💰 {self.current_player.name:<{self._NAME_W}} "
            f"+{self.turn_total:>{self._NUM_W}}  |  "
            f"Total = {self.current_player.score:>{self._NUM_W}}"
        )

        self._record_round_end()
        self.turn_total = 0

        if self.current_player.score >= self.win_score:
            print(f"\n🏆 {self.current_player.name} wins with {self.current_player.score} points!")
            if self.highscore is not None:
                self.highscore.add_score(
                    self.current_player.name, self.current_player.score
                )
            self.game_over = True

    def start(self) -> None:
        """Run the main game loop (interactive)."""
        # simple header
        print("╔" + "═" * 46 + "╗")
        print(f"║ 🎲 Two-Dice Pigs".ljust(46)+"║")
        print("╚" + "═" * 46 + "╝")
        print(f"👤 Player 1: {self.human_player.name}")
        print(f"🤖 Player 2: {self.computer_player.name}")
        print(f"\n➡️  {self.current_player.name} starts\n")

        cheat_choice = input("🧪 Cheat for faster testing? (y) ").lower().strip()
        if cheat_choice == "y":
            self.cheat()
        else:
            print("Playing fair is also cool i guess. ")

        while not self.game_over:
            if self.current_player is self.human_player:
                self.human_turn()
            else:
                self.computer_turn()

    def computer_turn(self) -> None:
        """Automate the computer player's turn using the AI policy."""
        while True:
            r1, r2, total = self.roll_dice()
            if not self.handle_roll(r1, r2, total):
                return

            projected = self.current_player.score + self.turn_total
            should_hold = self.computer_ai.decide(
                self.turn_total, projected, self.win_score
            )

            if should_hold:
                print(
                    f"🤖 {self.computer_player.name:<{self._NAME_W}} "
                    f"holds with {self.turn_total:>{self._NUM_W}}"
                )
                self.hold_and_check_win()
                if not self.game_over:
                    self.swap_turn()
                return

    def human_turn(self) -> None:
        """Run the human player's interactive turn."""
        while True:
            r1, r2, total = self.roll_dice()
            if not self.handle_roll(r1, r2, total):
                return
            user_choice = input("\n📝 Hold (h) or roll (enter)? ")
            if user_choice == "h":
                self.hold_and_check_win()
                if not self.game_over:
                    self.swap_turn()
                return

    def handle_roll(self, r1: int, r2: int, total: int) -> bool:
        """
        Handle the outcome of a dice roll.

        Returns:
            True if the player may continue the turn, False if turn ends.
        """
        if r1 == 1 and r2 == 1:
            print("🐍 Snake eyes! Your total score resets and your turn ends.")
            self.current_player.reset_score()
            self.turn_total = 0
            self._record_round_end()
            self.swap_turn()
            return False

        if r1 == 1 or r2 == 1:
            print("⚠️  Rolled a 1 — no points this turn.")
            self.turn_total = 0
            self._record_round_end()
            self.swap_turn()
            return False

        self.turn_total += total
        potential_score = self.current_player.score + self.turn_total
        #tidied uppp
        print(
            f"📈 Current turn total: {self.turn_total:>{self._NUM_W}}\n"
            f"😛 Potential score:    {potential_score:>{self._NUM_W}}"
        )
        return True

    def cheat(self) -> None:
        """Instantly give the human player a near-win score"""
        self.human_player.score = self.win_score - 1
        print(f"✨ {self.human_player.name} now has {self.human_player.score} points.")
