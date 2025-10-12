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
    
    def test_resturns_integer():
        """
        
        """
        dice = Die()
        result = dice.roll()
        assert isinstance(result, int)

    def test_default_sides_to_six():
        """
        
        """
        dice = Die()
        assert dice.sides == 6

    def test_rolls_are_different():
        """
        
        """
        dice = Die(6)
        results = set()
        for _ in range(50):
            results.add(dice.roll())
        assert len(results) > 1

    #  to-do: add test for remembering last roll





    