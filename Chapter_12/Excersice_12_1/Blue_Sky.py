import sys
import pygame
from settings import Settings

class BlueSky:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height)
        )

        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
    # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    game = BlueSky()
    game.run_game()