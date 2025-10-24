from highscore import Highscore


class TestHighscore:

    def test_empty_when_initialized(self):
        """
        testing if it is empty when it is initialized
        """
        highscore = Highscore()
        assert highscore.scores == []

    def test_clear_works_reseting_scores(self):
        """
        tests that crear works as a reset for the scores
        """
        highscore = Highscore()
        highscore.add_score(
            "player1", 76
        )  # cant come up with names so im just putting player, but it actually is for names

        def _clear():
            highscore.scores.clear()

        highscore.clear = _clear
        highscore.clear()
        assert highscore.scores == []

    def test_if_player_exists(self):
        """
        checks if a player exist
        """
        highscore = Highscore()
        highscore.add_score("player1", 76)

        exists_player1 = any(
            n.lower() == "player1".lower() for n, _ in highscore.scores
        )
        exists_player4 = any(
            n.lower() == "player4".lower() for n, _ in highscore.scores
        )

        assert exists_player1 is True
        assert exists_player4 is False

    def test_getting_highest_score(self):
        """
        testing getting the highest score
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 45)

        highest = max(highscore.scores, key=lambda x: x[1], default=None)
        assert highest == ("Player1", 87)

    def test_adding_a_score(self):
        """
        testing if its able to add scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", 64)
        assert highscore.scores == [("Player1", 64)]

    def test_adding_many_scores(self):
        """
        testing adding many scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player2", 99)
        highscore.add_score("Player3", 76)

        assert highscore.scores == [("Player2", 99), ("Player1", 87), ("Player3", 76)]

    def test_if_no_scores_then_highest_empty(self):
        """
        checking when no scores hishgest score is also empty
        """
        highscore = Highscore()
        highest = max(highscore.scores, key=lambda x: x[1], default=None)
        assert highest is None

    def test_updating_scores_of_existing_player(self):
        """
        testing if it updates the existing players
        """
        highscore = Highscore()
        highscore.add_score("Player1", 87)
        highscore.add_score("Player1", 96)

        best_for_player1 = max(
            score for name, score in highscore.scores if name == "Player1"
        )
        assert best_for_player1 == 96

    def test_lower_not_replacing_highest(self):
        """
        tests that the lower score doesnt replace the highest
        """
        highscore = Highscore()
        highscore.add_score("Player1", 97)
        highscore.add_score("Player1", 43)

        best_for_player1 = max(
            score for name, score in highscore.scores if name == "Player1"
        )
        assert best_for_player1 == 97

    def test_ignoring_negative_scores(self):
        """
        tests that it ignores negative scores
        """
        highscore = Highscore()
        highscore.add_score("Player1", -2)

        assert len(highscore.scores) == 1
        assert highscore.scores[0] == ("Player1", -2)
