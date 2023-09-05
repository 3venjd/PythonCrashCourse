import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Chapter_12\Exercise_12_6\imgs\ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_top = False
        self.moving_bottom = False
    
    def update(self):
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        if self.moving_top and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
