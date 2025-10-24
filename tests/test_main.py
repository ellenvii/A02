import types
import sys
import runpy
import importlib


def test_instructions_text_sanity():
    """
    Checking that the instructions include the key parts of the game rules.
    """
    import main

    text = main.instructions

    # make sure it mentions the main rules and features
    assert "Let's play a game." in text
    assert "Two-Dice Pigs" in text
    assert "roll 2 dice" in text or "You roll 2 dice" in text
    assert "single ⚀ is rolled" in text
    assert "2 ⚀ are rolled" in text
    assert "First to 100" in text


def test_main_prints_instructions_and_calls_cmdloop(monkeypatch, capsys):
    """
    Make sure main() prints the intro and actually runs Shell().cmdloop().
    """
    import main

    importlib.reload(main)

    called = {"cmdloop": 0}

    class DummyShell:
        def __init__(self):
            pass

        def cmdloop(self):
            called["cmdloop"] += 1

    # swap out shell.Shell with our dummy
    monkeypatch.setattr(main.shell, "Shell", DummyShell)

    # run the main() function
    main.main()

    out = capsys.readouterr().out
    # it should print the instructions
    assert main.instructions.strip() in out
    # and call cmdloop exactly once
    assert called["cmdloop"] == 1


def test_module_runs_when_invoked_as_script(monkeypatch, capsys):
    """
    Pretend we ran `python -m main` and check that it prints stuff and calls the cmdloop().
    """
    called = {"cmdloop": 0}

    class DummyShell:
        def __init__(self):
            pass

        def cmdloop(self):
            called["cmdloop"] += 1

    dummy_shell_module = types.SimpleNamespace(Shell=DummyShell)

    # trick Python into using our dummy shell when main imports it
    monkeypatch.setitem(sys.modules, "shell", dummy_shell_module)

    # run the module as if it was executed directly
    runpy.run_module("main", run_name="__main__")

    out = capsys.readouterr().out
    # make sure the output looks right
    assert "Let's play a game." in out
    assert called["cmdloop"] == 1
