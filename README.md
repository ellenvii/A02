# A02
Sustainable Methods Project


## Instructions for Pytest:

# Installation of Pytest

First make sure you have installed pytest through the terminal:

```bash
pip install pytest
```

# Running all tests

To be able to run all tests you only need to write "pytest" on the terminal

```bash
pytest
```

# Running specific files

If you are only interested on one file you can use the following, in this example we are going to use test_game.py

```bash
pytest tests/test_game.py
```

# Example of the output

```bash
===================================== short test summary info =====================================
FAILED tests/test_game.py::TestGame::test_rolling_one - AttributeError: 'Game' object has no attribute 'current_turn_points'
FAILED tests/test_game.py::TestGame::test_win_score_equal_100 - AttributeError: 'Game' object has no attribute 'hold'
FAILED tests/test_game.py::TestGame::test_end_game_finishes_turns - assert 44 == 0
=================================== 3 failed, 7 passed in 0.06s ===================================
```