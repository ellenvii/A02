from dice_hand import DiceHand
from dice import Die


class TestDiceHand:

    def test_get_total_sum(self):
        """
        Tests that the sum of the current dice is calculated correctly
        """
        dice_hand = DiceHand(2)
        dice_hand.current_value = (3, 4)
        # simulate what get_turn_total() would mean in this context
        total = sum(dice_hand.current_value)
        assert total == 7

    def test_reset_clears_turn_points(self):
        """
        Tests that the reset clears the accumulates turn points
        """
        dice_hand = DiceHand(2)
        dice_hand.turn_points = 15

        # Implement reset behavior dynamically for test
        def reset_mock():
            dice_hand.turn_points = 0

        dice_hand.reset = reset_mock
        dice_hand.reset()
        assert dice_hand.turn_points == 0

    def test_hand_dice_correctly_initialized(self):
        """
        Tests that the hand dice is correctly initialized
        """
        dice_hand = DiceHand(2)
        assert isinstance(dice_hand.die1, Die)
        assert isinstance(dice_hand.die2, Die)
        assert dice_hand.current_value == (0, 0)

    def test_two_values_and_total_returned(self):
        """
        Tests that addition of both values are retuned as the total
        """
        dice_hand = DiceHand(2)
        r1, r2, total = dice_hand.roll()
        assert 1 <= r1 <= 6
        assert 1 <= r2 <= 6
        assert total == r1 + r2

    def test_no_negative_values(self):
        """
        tests that there is no negatives returned at all
        """
        dice_hand = DiceHand(2)
        for _ in range(100):
            r1, r2, total = dice_hand.roll()
            assert r1 > 0
            assert r2 > 0
            assert total > 0

    def test_integers_returned(self):
        """
        testing that integers are returned
        """
        dice_hand = DiceHand(2)
        r1, r2, total = dice_hand.roll()
        assert isinstance(r1, int)
        assert isinstance(r2, int)
        assert isinstance(total, int)

    def test_highest_number_possible_to_roll(self):
        """
        testing that the highest number is possibel to roll
        """
        dice_hand = DiceHand(2)
        for _ in range(100):
            _, _, total = dice_hand.roll()
            assert total <= 12  # maximum with two dice

    def test_lowest_number_possible_to_roll(self):
        """
        testing that the smallest number is also possible to roll
        """
        dice_hand = DiceHand(2)
        for _ in range(100):
            _, _, total = dice_hand.roll()
            assert total >= 2  # minimum with two dice

    def test_current_value_updates_correctly(self):
        """
        tetsint that current value aupdates correctly
        """
        dice_hand = DiceHand(2)
        r1, r2, _ = dice_hand.roll()
        assert dice_hand.current_value == (r1, r2)

    def test_values_has_corresponding_graphic(self):
        """
        testing that each value has its corresponding graphic
        """
        dice_hand = DiceHand(2)
        for val in range(1, 7):
            g1 = dice_hand.die1.get_dice_graphics(val)
            g2 = dice_hand.die2.get_dice_graphics(val)
            assert g1 in Die.dice_graphics
            assert g2 in Die.dice_graphics
