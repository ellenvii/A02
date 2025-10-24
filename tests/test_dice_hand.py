"""
Dice Hand class testing
"""
from dice import Die
from dice_hand import DiceHand

class TestDiceHand:
    
    def test_get_total_sum(self):
        """
        Tests that the sum of the current dice is calculated correctly
        """
        dice_hand = DiceHand()
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

    def test_hand_dice_correctly_initialized(self):
        """
        Tests that the hand dice is correctly initialized
        """
        dice_hand = DiceHand()
        assert isinstance(dice_hand.die1, Die)
        assert isinstance(dice_hand.die2, Die)
        assert dice_hand.current_value == (0,0)

    def test_two_values_and_total_returned(self):
        """
        Tests that addition of both values are retuned as the total
        """
        dice_hand = DiceHand()
        r1, r2, total = dice_hand.roll()
        assert 1<= r1 <= 6
        assert 1<= r2 <= 6
        assert total == r1 + r2

    def test_no_negative_values(self):
        """
        tests that there is no negatives returned at all
        """
        dice_hand = DiceHand()
        for _ in range(100):
            r1, r2, total = dice_hand.roll()
            assert r1 > 0
            assert r2 > 0
            assert total > 0

    def test_integers_returned(self):
        """
        testing that integers are returned 
        """
        dice_hand = DiceHand()
        r1, r2, total = dice_hand.roll()
        assert isinstance(r1, int)
        assert isinstance(r2, int)
        assert isinstance(total, int)

    def test_highest_number_possible_to_roll(self):
        """
        testing that the highest number is possibel to roll
        """
        dice_hand = DiceHand()
        for _ in range(100):
            _, _, total = dice_hand.roll()
            assert total <= 6

    def test_lowest_number_possible_to_roll(self):
        """
        testing that the smallest number is also possible to roll
        """
        dice_hand = DiceHand()
        for _ in range(100):
            _, _, total = dice_hand.roll()
            assert total >= 1

    def test_current_value_updates_correctly(self):
       """
       tetsint that current value aupdates correctly 
       """
       dice_hand = DiceHand()
       r1, r2, _ = dice_hand.roll()
       assert dice_hand.current_value == (r1, r2)

    def test_values_has_corresponding_graphic(self):
        """
        testing that each value has its corresponding graphic
        """
        dice_hand = DiceHand()
        for val in range(1, 7):
            g1 = dice_hand.die1.get_dice_graphics(val)
            g2 = dice_hand.die2.get_dice_graphics(val)
            assert g1 in Die.dice_graphics
            assert g2 in Die.dice_graphics
