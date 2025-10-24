"""
Intelligence class testing
"""

class Intelligence:
    def test_resturns_either_roll_or_hold(self):
        """
        test that decite method returns either 'roll' or 'hold'
        """
        computer = Intelligence()         
        decision = computer.decide(current_turn_points=10, total_score=30, opp_score=25)        # oop = opponent
        assert decision in ["roll", "hold"]

    def test_different_difficulty_lvl_exist(self):
        """
        Test that computer intelligence supports multipple leves of difficulty
        """
        computer_easy = Intelligence(difficulty="easy")
        computer_medium = Intelligence(difficulty="medium")
        computer_hard = Intelligence(difficulty="hard")

        assert computer_easy.difficulty == "easy"
        assert computer_medium.difficulty == "medium"
        assert computer_hard.difficulty == "hard"

    def test_computer_holds_when_close_win(self):
        """
        Test that computer holds when is close to winning
        """
        computer = Intelligence()
        decision = computer.decide(current_turn_point=5, total_score=98, opponent_score=50)
        assert decision == "hold"

    def test_change_difficulty_while_game(self):
        """
        Test that it can be possible to change the difficulty of the computer intelligence during the game
        """
        computer = Intelligence()
        computer.set_dificulty("hard")
        assert computer.difficulty == "hard"

        decision = computer.decide(current_turn_points=15, total_score=30, opponent_score=30)
        assert decision == "roll"           # hard computer should know the score is low enough to be able to roll

    def test_computer_is_holding_when_ahead(self):
        """
        testing that computer holds when its ahead
        """
        computer = Intelligence(self)
        decision = computer.decide(current_turn_point=10, total_score=90, opponent_score=50)
        assert decision == "hold"
        
    def test_roll_when_opponent_close_win(self):
        """
        tests rolling when the opponen is closer to winning the game
        """
        computer = Intelligence()
        decision = computer.decide(current_turn_point=4, total_score=56, opponent_score=99)
        assert decision == "roll"

    def test_computer_being_cautios_by_holding(self):
        """
        tests computer is cautios and smart by holding 
        """
        computer = Intelligence(difficulty="hard")
        decision = computer.decide(current_turn_point=11, total_score=84, opponent_score=47)
        assert decision == "hold"

    def test_when_safe_computer_rolls(self):
        """
        testing if the computer hold when it seems safe to do so
        """
        computer = Intelligence()
        decision = computer.decide(current_turn_point=7, total_score=34, opponent_score=68)
        assert decision == "roll"

