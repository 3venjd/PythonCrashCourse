import sys
import pygame
from settings import Settings

class EmptyScreen:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
            self.settings.screen_height
            )
        )

        pygame.display.set_caption("Empty screen")
    
    def run_game(self):
        while True:
            self.check_events()
    

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_LEFT:
            print("the left key was pressed")
        elif event.key == pygame.K_UP:
            print("the Up key was pressed")
        elif event.key == pygame.K_RIGHT:
            print("the right key was pressed")
        elif event.key == pygame.K_DOWN:
            print("the down key was pressed")
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_LEFT:
            print("the left key was released")
        elif event.key == pygame.K_UP:
            print("the Up key was released")
        elif event.key == pygame.K_RIGHT:
            print("the right key was released")
        elif event.key == pygame.K_DOWN:
            print("the down key was released")
        elif event.key == pygame.K_q:
            sys.exit()

if __name__ == '__main__':
    rl = EmptyScreen()
    rl.run_game()

