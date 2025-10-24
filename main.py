# Could technically just have shell.py instead of main,
# but will call shell from main.

import shell

"""
Main class to call on shell and create loop.
"""

instructions = (
    "\nLet's play a game.\n"
    "Two-Dice Pigs involves collecting as many points as possible.\n"
    "You roll 2 dice, if niether show ⚀, add those points to your score.\n"
    "You may roll again, or choose to hold.\n"
    "If a single ⚀ is rolled, you score nothing and your turn ends.\n"
    "If 2 ⚀ are rolled, your score resets and your turn ends.\n"
    "First to 100 wins!\n"
)


def main():
    print(instructions)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
