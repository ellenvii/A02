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
    
    def test_resturns_integer(self):
        """
        
        """
        dice = Die()
        result = dice.roll()
        assert isinstance(result, int)

    def test_default_sides_to_six(self):
        """
        
        """
        dice = Die()
        assert dice.sides == 6

    def test_rolls_are_different(self):
        """
        
        """
        dice = Die(6)
        results = set()
        for _ in range(50):
            results.add(dice.roll())
        assert len(results) > 1

    def test_las_roll_is_remembered(self):
        """
        
        """
        dice = Die()
        rolled_value = dice.roll()
        assert dice.last_roll == rolled_value

    # Some error handling tests
    def test_invalid_sides_are_rejected(self):
        """
        
        """
        try:
            dice = Die(1)
            assert False, "Raising error for 1 side"
        except ValueError:
            assert True
        
    def test_negative_sides_are_rejected(self):
        """
        
        """
        try:
            dice = Die(-5)
            assert False, "Raising error for negative sides"
        except ValueError:
            assert True


    