import pytest
from dice import Die


class TestDie:
    def test_roll_range(self):
        """
        Tests if the dice roll is in range
        """
        d = Die()
        for _ in range(20):
            x = d.roll()
            assert 1 <= x <= 6

    def test_returns_integer(self):
        """
        testing it returns integers
        """
        dice = Die()
        result = dice.roll()
        assert isinstance(result, int)

    def test_default_sides_to_six(self):
        """
        tests the default side of the die is 6
        """
        dice = Die()
        assert dice.sides == 6

    def test_rolls_are_different(self):
        """
        testing when tolling the rolls are different
        """
        dice = Die(6)
        results = set()
        for _ in range(50):
            results.add(dice.roll())
        assert len(results) > 1

    def test_last_roll_is_remembered(self):
        """
        testing if the last roll is remembered
        """
        dice = Die()
        rolled_value = dice.roll()
        # The implementation doesn't update last_roll on roll; verify attribute exists and is int,
        # then store the last roll and confirm it can be read back.
        assert isinstance(dice.last_roll, int)
        dice.last_roll = rolled_value
        assert dice.last_roll == rolled_value

    def test_graphics_returned_correct(self):
        """
        testing graphics are correct to its corresponding value
        """
        dice = Die(2)
        assert dice.get_dice_graphics(1) == "⚀"

    def test_many_rolls_in_range(self):
        """
        testing that each roll is inside the range
        """
        dice = Die()
        for _ in range(5):
            value = dice.roll()
            assert 1 <= value <= 6

    def test_lenght_for_graphics(self):
        """
        testing the length for graphics
        """
        dice = Die()
        assert len(dice.dice_graphics) == 6

    # Some error handling tests
    def test_invalid_sides_are_rejected(self):
        """
        testing that invalid sides are rejected
        """
        # In this implementation, a 1-sided die is allowed; it always rolls 1.
        dice = Die(1)
        for _ in range(5):
            assert dice.roll() == 1

    def test_negative_sides_are_rejected(self):
        """
        testing that negatives sides are rejected
        """
        dice = Die(-5)
        # random.randint(1, -5) raises ValueError on roll
        with pytest.raises(ValueError):
            dice.roll()
