from player import Player

class TestPlayer:
    """
    Test cases for the Player class functionality
    """
    # Player name tests
    def test_player_init_name(self):
        """
        Test that player is initialized with correct name
        """
        player = Player("Johan")
        assert player.name == "Johan"
    
    def test_player_can_change_name(self):
        """
        Test that player can change name to another value
        """
        player = Player("Name before")
        player.set_name("New Name")
        assert player.name == "New Name"

    def test_player_name_is_string(self):
        """
        Test that player name is always stored as string
        """
        player = Player("Player 1")
        assert isinstance(player.name, str)
    
    # Score management tests
    def test_player_can_add_points(self):
        """
        Test that points can be added to player score
        """
        player = Player("Tester")
        player.add_points(10)
        assert player.score == 10

    def test_player_accumulates_points_correctly(self):
        """
        Test that points accumulate correctly with multiple additions
        """
        player = Player("Tester")
        player.add_points(5)
        player.add_points(15)
        assert player.score == 20

    def test_player_can_reset_score(self):
        """
        Test that player score can be reset to 0
        """
        player = Player("Tester")
        player.add_points(12)
        player.reset_score()
        assert player.score == 0

    def test_score_is_integer(self):
        """
        Test that score is always an integer value
        """
        player = Player("Player1")
        player.add_points(3)
        assert isinstance(player.score, int)

    # Game state representation tests
    def test_player_str_representation(self):
        """
        Test that string representation includes player name and score
        """
        player = Player("Tester")
        player.add_points(10)
        text = str(player)
        assert "Tester" in text
        assert "10" in text
    
    # Error handling tests
    def test_player_cannot_add_negative_points(self):
        """
        Test that adding negative points raises ValueError
        """
        player = Player("Tester")
        try:
            player.add_points(-5)
            assert False, "Expected exception for negative points"
        except ValueError:
            assert True
    
    def test_default_player_score(self):
        """
        Tests that default player score is 0
        """
        player = Player("mamahuevo")
        assert player.score == 0