import types
import pytest

from intelligence import Intelligence

#Test helpers

class DummyPlayer:
    def __init__(self, score):
        self.score = score

def make_ai(score=0, difficulty="normal"):
    return Intelligence(DummyPlayer(score), difficulty=difficulty)

#Actual tests

def test_decide_returns_bool():
    """
    decide() returns a boolean: True = 'hold', False = 'roll'
    """
    ai = make_ai(score=30, difficulty="normal")
    decision = ai.decide(turn_total=10, potential_score=40, win_score=100)
    assert isinstance(decision, bool)

def test_different_difficulty_levels_exist():
    """
    Computer intelligence supports multiple difficulty levels.
    Note: implementation recognizes 'easy', 'hard', and uses 'normal' as default/other.
    """
    ai_easy = make_ai(difficulty="easy")
    ai_normal = make_ai(difficulty="normal")
    ai_hard = make_ai(difficulty="hard")

    assert ai_easy.difficulty == "easy"
    assert ai_normal.difficulty == "normal"
    assert ai_hard.difficulty == "hard"

def test_computer_holds_when_close_to_winning():
    """
    If potential_score >= win_score, AI always holds (returns True).
    """
    ai = make_ai(score=75)
    assert ai.decide(turn_total=1, potential_score=100, win_score=100) is True

def test_change_difficulty_during_game(monkeypatch):
    """
    Difficulty can be changed during play by setting the attribute.
    For deterministic behavior, patch random.randint to 0.
    """
    # Thresholds with randint=0: easy=10, normal=18, hard=25 (plus +2 if player.score < 50)
    monkeypatch.setattr("random.randint", lambda a, b: 0)

    ai = make_ai(score=30, difficulty="normal")
    ai.difficulty = "hard"  # change difficulty mid-game

    # player.score < 50 adds +2 → hard hold_at = 27
    # turn_total below 27 → should roll (False)
    decision = ai.decide(turn_total=15, potential_score=45, win_score=100)
    assert decision is False  # 'roll'

def test_computer_holds_when_turn_total_exceeds_threshold(monkeypatch):
    """
    With a sufficiently high turn_total, AI holds.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 0)

    ai = make_ai(score=80, difficulty="normal")  # score >= 50 → no +2 risk tweak
    # normal hold_at = 18; turn_total = 25 ≥ 18 → hold
    decision = ai.decide(turn_total=25, potential_score=90, win_score=100)
    assert decision is True  # 'hold'

def test_roll_when_below_threshold(monkeypatch):
    """
    If turn_total is below threshold, AI rolls.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 0)

    ai = make_ai(score=80, difficulty="normal")  # normal hold_at = 18
    decision = ai.decide(turn_total=4, potential_score=56, win_score=100)
    assert decision is False  # 'roll'

def test_hard_ai_can_be_cautious_and_hold(monkeypatch):
    """
    Hard AI uses a higher threshold; verify a big turn_total leads to holding.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 0)

    ai = make_ai(score=40, difficulty="hard")  # score < 50 → +2
    # hard hold_at = 25 + 2 = 27; 30 ≥ 27 → hold
    decision = ai.decide(turn_total=30, potential_score=84, win_score=100)
    assert decision is True  # 'hold'

def test_when_safe_computer_rolls(monkeypatch):
    """
    With a small turn_total and normal difficulty (risk tweak active), AI rolls.
    """
    monkeypatch.setattr("random.randint", lambda a, b: 0)

    ai = make_ai(score=34, difficulty="normal")  # score < 50 → +2
    # normal hold_at = 18 + 2 = 20; 7 < 20 → roll
    decision = ai.decide(turn_total=7, potential_score=34, win_score=100)
    assert decision is False  # 'roll'
