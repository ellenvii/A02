"""
Dice class testing
"""

from dice import Die

class TestDie:
    """
    Tests if the dice roll is in range
    """
    def test_roll_range(self):
        d = Die()
        for i in range(20):
            x = d.roll()
            assert 1 <= x <= 6
    
