highScore = 'high_score.txt'

class GameStats:
    """Track stats throughout the game"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start game in active state
        self.game_active = False

        # High score should never be reset
        with open(highScore) as file_obj:
            self.high_score = int(file_obj.read())

    def reset_stats(self):
        """Initialise statistics that can change during gameplay"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1