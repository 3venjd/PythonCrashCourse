class GameStats:
    """Track statisctics for Alien Invasion"""

    def __init__(self,ai_game):
        """Initiañize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start Alien Invasion in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit