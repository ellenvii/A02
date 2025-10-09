"""
Import class here
"""
class TestGame:
    def test_rolling_one(self): 
        """
        Test when 1 is rolled the turn ends and give 0 points
        """
        game = Game("Player1", "player2")
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
        game = Game("Player1", "Player2")
        assert game.player1.score == 0
        assert game.player1.score == 0