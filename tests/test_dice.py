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
    
    def test_returns_integer(self):
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

    def test_last_roll_is_remembered(self):
        """
        
        """
        dice = Die()
        rolled_value = dice.roll()
        assert dice.last_roll == rolled_value
    
    def test_graphics_returned_correct():
        dice = Die(2)
        assert dice.get_dice_graphics(1) == '⚀'

    def test_many_rolls_in_range():
        dice = Die()
        for _ in range(5):
            value = dice.roll()
            assert 1 <= value <= 6

    def test_lenght_for_graphics():
        dice = Die()
        assert len(dice.dice_graphics) == 6

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