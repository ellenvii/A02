"""
Game class testing
"""

from game import Game

class TestGame:
    def test_rolling_one(self): 
        """
        Test when 1 is rolled the turn ends and give 0 points
        """
        game = Game("Human player", "Computer player")
        initial_score = game.human_player.score
        game.roll_dice() # assumption of this returning 1
        assert game.current_turn_points == 0
        assert game.human_player.score == initial_score

    def test_win_score_equal_100(self):
        """
        Test when score has reached 100 points game is over
        """
        game = Game("Winner", "Loser")
        game.cheat() # this should put player near winning score
        game.roll_dice()
        game.hold()
        assert game.winner == game.human_player
        assert game.game_over == True

    def test_start_game_at_zero_scores(self): 
        """
        Test both players start with 0 score
        """
        game = Game("human player", "computer player")
        assert game.human_player.score == 0
        assert game.computer_player.score == 0

    def test_turn_swaps(self):
        """
        Testing that each turn theres a swap
        """
        game = Game("Human player", "Computer player")
        game.swap_turn()
        assert game.current_player == game.computer_player
        assert game.turn_total == 0

    def test_dice_roll_returning_tuple(self):
        """
        tests that dice retunrs tuple heheh
        """
        game = Game("Human player", "Computer player")
        result = game.roll_dice()
        assert isinstance(result, tuple)
        assert len(result) == 3                 # (r1, r2, total) 

    def test_end_game_finishes_turns(self):
        """
        Tests that ending a game fineshes a turn
        """
        game = Game("Human player", "Computer player")
        game.game_over = True
        start_score = game.current_player.score
        game.computer_turn()
        assert game.current_player.score == start_score

    def test_rolling_snake_eyes(self):
        """
        Tests the scenario of rolling a snake eyes
        """
        game = Game("Human player", "Computer player")
        game.current_player.score == 43
        result = game.handle_roll(1, 1, 2)
        assert result is False
        assert game.current_player == game.computer_player      # next player turn
        assert game.other_player.score == 0                     # previous player (human) resets to 0

    def test_turn_total(self):
        """
        Testing total of turns are accumulated 
        """
        game = Game("Human player", "Computer player")
        game.handle_roll(2, 4, 6)
        game.handle_roll(4, 5, 9)
        assert game.turn_total == 15

    def test_hold_not_ending_game(self):
        """
        tests holding doesnt end the game
        """
        game = Game("Human player", "Computer player")
        game.turn_total = 17
        game.hold_and_check_win()
        assert game.game_over is False

    def test_hold_right_before_winning(self):
        """
        testing hold before winning
        """
        game = Game("Human player", "Computer player")
        game.current_player.add_points(96)
        game.turn_total = 4
        game.hold_and_check_win()
        assert game.game_over is True
        assert game.current_player.score >= game.win_score