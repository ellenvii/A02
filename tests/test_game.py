from game import Game
from highscore import Highscore

class TestGame:
    def test_rolling_one(self): 
        """
        Test when 1 is rolled the turn ends and give 0 points
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        initial_score = game.human_player.score
        # Explicitly simulate a roll containing a single 1
        result = game.handle_roll(1, 4, 5)
        assert result is False
        assert game.turn_total == 0
        # Human’s score didn’t change for a single 1
        assert game.other_player.score == initial_score  # after handle_roll swap, other_player is the human

    def test_win_score_equal_100(self):
        """
        Test when score has reached 100 points game is over
        """
        game = Game("Winner", "Loser", highscore=Highscore())
        # Put human near winning score and then hold to cross 100
        game.current_player.add_points(99)
        game.turn_total = 1
        game.hold_and_check_win()
        assert game.game_over is True
        # After hold_and_check_win, turn is NOT swapped; current_player is the winner
        assert game.current_player.score >= game.win_score

    def test_start_game_at_zero_scores(self): 
        """
        Test both players start with 0 score
        """
        game = Game("human player", "computer player", highscore=Highscore())
        assert game.human_player.score == 0
        assert game.computer_player.score == 0

    def test_turn_swaps(self):
        """
        Testing that each turn theres a swap
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        # Starts on human; after swap it should be computer and turn_total reset
        game.swap_turn()
        assert game.current_player == game.computer_player
        assert game.turn_total == 0

    def test_dice_roll_returning_tuple(self):
        """
        tests that dice retunrs tuple heheh
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        result = game.roll_dice()
        assert isinstance(result, tuple)
        assert len(result) == 3                 # (r1, r2, total) 

    def test_end_game_finishes_turns(self):
        """
        Tests that ending a game fineshes a turn
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        start_score = game.current_player.score

        # Make computer_turn deterministic and non-scoring by forcing a single-1 roll
        game.roll_dice = lambda: (1, 3, 4)
        game.game_over = True  # original intent: once game is over, turns effectively do nothing
        game.computer_turn()
        # With a forced 1, handle_roll ends the turn with 0 banked; score unchanged
        assert game.current_player.score == start_score

    def test_rolling_snake_eyes(self):
        """
        Tests the scenario of rolling a snake eyes
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        # Give the human some points so we can see them reset to 0
        game.current_player.add_points(43)
        result = game.handle_roll(1, 1, 2)
        assert result is False
        # After snake eyes, current player is swapped to computer
        assert game.current_player == game.computer_player
        # The previous player (human) should have been reset to 0
        assert game.other_player.score == 0

    def test_turn_total(self):
        """
        Testing total of turns are accumulated 
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        game.handle_roll(2, 4, 6)  # no 1s → accumulates
        game.handle_roll(4, 5, 9)  # no 1s → accumulates
        assert game.turn_total == 15

    def test_hold_not_ending_game(self):
        """
        tests holding doesnt end the game
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        game.turn_total = 17
        game.hold_and_check_win()
        assert game.game_over is False


    def test_hold_right_before_winning(self):
        """
        testing hold before winning
        """
        game = Game("Human player", "Computer player", highscore=Highscore())
        game.current_player.add_points(96)
        game.turn_total = 4
        game.hold_and_check_win()
        assert game.game_over is True
        assert game.current_player.score >= game.win_score  # after holding, other_player is the human who just scored
