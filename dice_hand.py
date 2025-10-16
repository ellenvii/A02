from dice import Die

class DiceHand:

    def __init__(self, num_of_dice):    
        """Constructor"""   
        
        self.die1 = Die()
        self.die2 = Die()
        self.current_value = (0, 0)

    def roll(self):
        """Rolls dice"""
        r1 = self.die1.roll()
        r2 = self.die2.roll()
        self.current_value = (r1, r2)
        g1 = self.die1.get_dice_graphics(r1)
        g2 = self.die2.get_dice_graphics(r2)
        total = r1 + r2 
        print(f'You rolled {g1} {g2} ({r1}+{r2}={total})! ')
        return r1, r2, total
    
    
