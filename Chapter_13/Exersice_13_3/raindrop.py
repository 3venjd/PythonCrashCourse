import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('Chapter_13\\Exersice_13_3\\img\\raindrop.bmp')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
    
    def update(self):
        self.y += (self.settings.raindrop_speed * self.settings.rain_direction)
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True