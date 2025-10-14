"""
Dice Hand class testing
"""

from dice_hand import DiceHand

class TestDiceHand:
    def test_get_total_sum(self):
        """
        Tests that the sum of the current dice is calculated correctly
        """
        dice_hand = DiceHand(2)
        dice_hand.current_value = [3, 4]
        assert dice_hand.get_turn_total() == 7

    def test_reset_clears_turn_points(self):
        """
        Tests that the reset clears the accumulates turn points
        """
        dice_hand = DiceHand()
        dice_hand.turn_points = 15
        dice_hand.reset()
        assert dice_hand.turn_points == 0