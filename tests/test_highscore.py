"""
Highscore class testing
"""

from highscore import Highscore

class TestHighscore:

    def test_empty_when_initialized():
        """
        testing if it is empty when it is initialized
        """
        highscore = Highscore()
        assert highscore.scores == []

    def test_clear_works_reseting_scores():
        """
        tests that crear works as a reset for the scores
        """
        highscore = Highscore()
        highscore.add_score("player1", 76)          # cant come up with names so im just putting player, but it actually is for names
        highscore.clear()
        assert highscore.scores == []

    def test_if_player_exists():
        """
        checks if a player exist
        """
        highscore = Highscore()
        highscore.add_score("player1", 76)
        assert highscore.player_exists("Player1") is True
        assert highscore.player_exists("Player4") is False

    def test_getting_highest_score():
        """
        testing getting the highest score
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 45)
        highest = highscore.get_highest_score()
        assert highest == ("Player1", 87)

    def test_adding_a_score():
        """
        testing if its able to add scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", 64)
        assert highscore.scores == [("Player1", 64)]

    def test_adding_many_scores():
        """
        testing adding many scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 99)
        highscore.add_score("Player3", 76)
        assert highscore.scores == [("Player1", 87), ("Player2", 99), ("Player3", 76)]

    def test_if_no_scores_then_highest_empty():
        """
        checking when no scores hishgest score is also empty
        """
        highscore = Highscore()
        assert highscore.get_highest_score() is None

    def test_updating_scores_of_existing_player():
        """
        testing if it updates the existing players
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player1", 96)
        assert highscore.get_highest_score == ("Player", 96)

    def test_lower_not_replacing_highest():
        """
        tests that the lower score doesnt replace the highest 
        """
        highscore = Highscore()
        highscore.add_score("Player1", 97)
        highscore.add_score("Player1", 43)
        assert highscore.get_highest_score == ("Player1", 97)

    def test_ignoring_negative_scores():
        """
        tests that it ignores negative scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", -2)
        assert len(highscore.scores) == 0
