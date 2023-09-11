import sys
import pygame
from settings import Settings
from raindrop import Raindrop
from random import random,randint
import time

class fullRain:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Rain")

        self.raindrop = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrop.draw(self.screen)

        pygame.display.flip()

    def _create_rain(self):
        raindrop = Raindrop(self)
        imageWidth = raindrop.image.get_width()
        imageHeight = raindrop.image.get_height()

        for i in range(10):            
            randomXPositionRaindrop = randint(0, self.settings.screen_width - imageWidth)
            randomYPositionRaindrop = randint(0, self.settings.screen_height - imageHeight)
            self._create_raindrop(randomXPositionRaindrop, randomYPositionRaindrop)
            
        
    
    def _create_raindrop(self, column, row):
        raindrop = Raindrop(self)
        raindrop.rect.x = column
        raindrop.rect.y = row
        self.raindrop.add(raindrop)

    def _update_raindrops(self):
        
        for raindrop in self.raindrop.copy():
            if raindrop.rect.bottom >= self.settings.screen_height:
                self.raindrop.remove(raindrop)
        
        self._create_rain()
        self.raindrop.update()
        

if __name__ == '__main__':
    game = fullRain()
    game.run_game()
        