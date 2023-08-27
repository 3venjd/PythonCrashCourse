import pygame
from settings import Setting
from palace import palace
import sys

class GCharacter():

    def __init__(self):
        pygame.init()

        self.settings = Setting()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_witdh,
             self.settings.screen_heigth)
            )
        pygame.display.set_caption("Floating Palace")

        self.palace = palace(self)

    def run_game(self):
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
        self.palace.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game 
    ai = GCharacter()
    ai.run_game()
