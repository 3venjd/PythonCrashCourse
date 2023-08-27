import sys
import pygame
from settings import Settings
from ship import Ship

class AlienIvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #use a helpers method to allow manage events separately
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during  each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game 
    ai = AlienIvasion()
    ai.run_game()

        