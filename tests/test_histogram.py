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

    def test_adding_same_roll_multiple_times(self):
        histogram = Histogram()
        for _ in range(5):
            histogram.add_roll(4)
            assert histogram.get_count(4) == 5

    def test_can_add_more_rolls_after_reset(self):
        histogram = Histogram()
        histogram.add_roll(5)
        histogram.reset()
        histogram.add_roll(2)
        assert histogram.get_count(2) == 1
        assert histogram.total_rolls == 1

    def test_empty_equals_zero(self):
        histogram = Histogram()
        assert histogram.total_rolls == 0

    def test_not_valid_roll_dont_change_anything(self):
        histogram = Histogram()
        histogram.add_roll(1) # nit valid total, there are 2 dices on each hand
        histogram.add_roll(13) #not valid either
        for i in range(2, 13):
            assert histogram.get_count(i) == 0
        assert histogram.total_rolls == 0


    def test_adding_different_totals(self):
        histogram = Histogram()
        rolls = [2, 5, 7, 12, 5]
        for r in rolls:
            histogram.add_roll()
        assert histogram.get_count(2) == 1
        assert histogram.get_count(5) == 2
        assert histogram.get_count(7) == 1
        assert histogram.get_count(12) == 1
        assert histogram.total_rolls == 5

    # out of ideas to test more for now...
    # def test():
    #     pass

    # def test():
    #     pass