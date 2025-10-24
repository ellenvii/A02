# A02
Sustainable Methods Project

# Two-Dice Pigs

Two-Dice Pigs involves collecting as many points as possible.
You roll two dice — if neither shows ⚀, add those points to your score.
You may roll again or choose to hold.
If a single ⚀ is rolled, you score nothing and your turn ends.
If two ⚀ are rolled, your score resets and your turn ends.
First to 100 wins!

# Game Intelligence Implementation

Before starting the game, you may choose difficulty of easy, normal or hard.
By default, it is normal.
Easy entails that it will hold atv a lower number, with normal and hard holding at higher numbers. 
To change difficulty, typing 'difficulty hard' before starting will change the difficulty to hard.
The same goes for easy and normal.

# Project Structure
```bash
A02/
├── docs/                # Generated documentation (by using pdoc)
├── tests/               # Unit tests for all classes 
├── main.py              
├── shell.py             
├── dice.py              
├── player.py            
├── highscore.py         
├── README.md            # Project instructions 
└── requirements.txt     
```

# The Setup and Installation of the Game
1. Unzip the file. If you are on windows use right click and then "extract all". For macOS users just double click on the zip file to unzip.
2. Now open the folder in VS Code or in the terminal.
```bash
cd path/to/A02
```

# How to Run the Game
Once inside the folder A02, run the following code in the terminal:
```bash
python3 main.py
```
Then you only need to follow the instructions fo the game and just have fun!

# Instructions for Pytest:

## Installation of Pytest
First make sure you have installed pytest through the terminal:

```bash
pip install pytest          # macOS
pip install pytest          # Windows
```

## Running all tests
To be able to run all tests you only need to write "make pytest" in the terminal.

```bash
make pytest
```

## Running specific files
If you are only interested on one file you can use the following, in this example we are going to use test_game.py

```bash
pytest tests/test_game.py
```

## Example of the output
```bash
===================================== short test summary info =====================================
FAILED tests/test_game.py::TestGame::test_rolling_one - AttributeError: 'Game' object has no attribute 'current_turn_points'
FAILED tests/test_game.py::TestGame::test_win_score_equal_100 - AttributeError: 'Game' object has no attribute 'hold'
FAILED tests/test_game.py::TestGame::test_end_game_finishes_turns - assert 44 == 0
=================================== 3 failed, 7 passed in 0.06s ===================================
```

# Generate UML

```bash
make pyreverse
```

# Generate PyDocs

```bash
make pydoc
```

# Checking Coverage and Generating Report

```bash
make coverage
```

