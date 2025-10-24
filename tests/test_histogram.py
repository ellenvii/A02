import io
import sys
from histogram import Histogram


class DummyPlayer:
    def __init__(self, name):
        self.name = name


class TestHistogram:
    def test_initialization_starts_empty(self):
        """
        Test that Histogram initializes with an empty data list.
        """
        player = DummyPlayer("Player1")
        histogram = Histogram(player)
        assert histogram.player == player
        assert histogram.data == []

    def test_add_entry_adds_tuple(self):
        """
        Test that add_entry correctly appends a (round_number, score) tuple.
        """
        histogram = Histogram("Computer")
        histogram.add_entry(1, 25)
        histogram.add_entry(2, 40)
        assert histogram.data == [(1, 25), (2, 40)]

    def test_show_prints_histogram_output(self, capsys):
        """
        Test that show() prints the expected histogram text.
        """
        player = DummyPlayer("Tester")
        histogram = Histogram(player)
        histogram.add_entry(1, 10)
        histogram.add_entry(2, 30)

        histogram.show()
        captured = capsys.readouterr().out

        assert "Histogram for Tester" in captured
        assert "Round  1:" in captured
        assert "Round  2:" in captured
        assert "(10 pts)" in captured
        assert "(30 pts)" in captured
        assert "#" in captured

    def test_histogram_bar_length_is_score_divided_by_five(self, capsys):
        """
        Test that the number of '#' symbols corresponds to score // 5.
        """
        histogram = Histogram("Player")
        histogram.add_entry(1, 25)  # 25 // 5 = 5 hashes
        histogram.add_entry(2, 7)   # 7 // 5 = 1 hash (min 1)

        histogram.show()
        captured = capsys.readouterr().out.splitlines()

        # Extract bars
        bars = [line for line in captured if line.strip().startswith("Round")]
        assert "#####" in bars[0]  # 5 hashes for 25 points
        assert "#" in bars[1] and "##" not in bars[1]  # exactly 1 hash for 7 points

    def test_show_uses_player_name_if_exists(self, capsys):
        """
        Test that show() uses player's name if the object has one.
        """
        player = DummyPlayer("Alex")
        histogram = Histogram(player)
        histogram.add_entry(1, 15)

        histogram.show()
        captured = capsys.readouterr().out
        assert "Histogram for Alex" in captured

    def test_show_fallback_to_str_if_no_name(self, capsys):
        """
        Test that show() falls back to str(player) if player has no 'name' attribute.
        """
        histogram = Histogram("AI_Bot")
        histogram.add_entry(1, 20)
        histogram.show()
        captured = capsys.readouterr().out
        assert "Histogram for AI_Bot" in captured

    def test_multiple_rounds_stored_in_order(self):
        """
        Test that entries preserve the correct order of rounds.
        """
        histogram = Histogram("CPU")
        rounds = [(1, 10), (2, 15), (3, 22)]
        for r, s in rounds:
            histogram.add_entry(r, s)
        assert histogram.data == rounds

    def test_show_prints_separator_lines(self, capsys):
        """
        Test that show() includes separator lines of dashes before and after the bars.
        """
        histogram = Histogram("CPU")
        histogram.add_entry(1, 10)
        histogram.show()
        captured = capsys.readouterr().out
        assert "----------------------------------------" in captured
