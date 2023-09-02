import pygame

class rocket:

    def __init__(self,rocket_game):
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings

        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load('Chapter_12\Exercise_12_4\Imgs\Rocket.bmp')
        self.image = pygame.transform.scale(self.image,(60, 70))
        self.rect = self.image.get_rect()
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_top = False
        self.moving_right = False
        self.moving_bottom = False
    
    
    def update(self):

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        
        if self.moving_top and self.rect.top > 0 :
            self.y -= self.settings.rocket_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)