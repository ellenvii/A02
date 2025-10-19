"""
Highscore class testing
"""

from highscore import Highscore

class TestHighscore:

    def test_empty_when_initialized():
        highscore = Highscore()
        assert highscore.scores == []

    def test_clear_works_reseting_scores():
        highscore = Highscore()
        highscore.add_score("player1", 76)          # cant come up with names so im just putting player, but it actually is for names
        highscore.clear()
        assert highscore.scores == []

    def test_if_player_exists():
        highscore = Highscore()
        highscore.add_score("player1", 76)
        assert highscore.player_exists("Player1") is True
        assert highscore.player_exists("Player4") is False

    def test_getting_highest_score():
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 45)
        highest = highscore.get_highest_score()
        assert highest == ("Player1", 87)

    def test_adding_a_score():
        highscore = Highscore()
        highscore.add_score("Player1", 64)
        assert highscore.scores == [("Player1", 64)]

    def test_adding_many_scores():
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 99)
        highscore.add_score("Player3", 76)
        assert highscore.scores == [("Player1", 87), ("Player2", 99), ("Player3", 76)]

    def test_if_no_scores_then_highest_empty():
        highscore = Highscore()
        assert highscore.get_highest_score() is None

    def test_updating_scores_of_existing_player():
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player1", 96)
        assert highscore.get_highest_score == ("Player", 96)

    def test_lower_not_replacing_highest():
        highscore = Highscore()
        highscore.add_score("Player1", 97)
        highscore.add_score("Player1", 43)
        assert highscore.get_highest_score == ("Player1", 97)

    def test_ignoring_negative_scores():
        highscore = Highscore()
        highscore.add_score("Player1", -2)
        assert len(highscore.scores) == 0
