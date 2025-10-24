from dice import Die


class DiceHand:
    """Represents 2 dice rolle during the current turn"""

    def __init__(self, num_of_dice):
        """Constructor"""
        self.die1 = Die()
        self.die2 = Die()
        self.current_value = (0, 0)

    def roll(self):
        """Returns roll 1, roll 2 and the total"""
        r1 = self.die1.roll()
        r2 = self.die2.roll()
        self.current_value = (r1, r2)  # tuple of rolls
        g1 = self.die1.get_dice_graphics(r1)
        g2 = self.die2.get_dice_graphics(r2)
        total = r1 + r2
        print(f"\nYou rolled {g1} {g2} ({r1}+{r2}={total})! ")
        return r1, r2, total
