class GameStats:
    """Track stats throughout the game"""

    def __init__(self, ai_game):
        """Initialise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start game in active state
        self.game_active = False

    def reset_stats(self):
        """Initialise statistics that can change during gameplay"""
        self.ships_left = self.settings.ship_limit
        self.score = 0