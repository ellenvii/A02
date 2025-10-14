"""
Intelligence class testing
"""

class Intelligence:
    def test_resturns_either_roll_or_hold(self):
        """
        test that decite method returns either 'roll' or 'hold'
        """
        computer = Intelligence         # wasn't sure if call it computer or ai
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
        computer = Intelligence(difficulty="medium")
        decision = computer.decide(current_turn_point=5, total_score=98, opponent_score=50)
        assert decision == "hold"

    def test_change_difficulty_while_game(self):
        """
        Test that it can be possible to change the difficulty of the computer intelligence during the game
        """
        computer = Intelligence(difficulty="easy")
        computer.set_dificulty("hard")
        assert computer.difficulty == "hard"

        decision = computer.decide(current_turn_points=15, total_score=30, opponent_score=30)
        assert decision == "roll"           # hard computer should know the score is low enough to be able to roll




