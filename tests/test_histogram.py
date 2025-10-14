"""
Histogram class testing
"""

from histogram import Histogram

class TestHistogram:
    def test_initialization_with_zeros(self):
        """
        
        """
        histogram = Histogram()
        for value in range(1,7):
            assert histogram.get_count(value) == 0
        
    def test_correct_range_when_initialize(self):
        """
        
        """
        histogram = Histogram()
        assert histogram.min_value == 1
        assert histogram.max_value == 6

    def test_ability_to_add_single_roll(self):
        """
        
        """
        histogram = Histogram()
        histogram.add_roll(3)
        assert histogram.get_count(3) == 1

    def test_reset_working(self):
        """
        
        """
        histogram = Histogram()
        histogram.add_roll(1)
        histogram.add_roll(2)
        histogram.add_roll(3)
        histogram.reset()
        assert histogram.total_rolls == 0
        for value in range(1,7):
            assert histogram.get_count(value) == 0