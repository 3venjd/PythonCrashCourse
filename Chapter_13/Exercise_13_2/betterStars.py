import sys
import pygame
from settings import Settings
from star import Star
from random import randint


class betterStars:

    def __init__(self):
        pygame.init()

        self.setting = Settings()
        self.screen = pygame.display.set_mode(
            (
                self.setting.screen_width,
                self.setting.screen_height
            )
        )

        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Better Stars')

        self.star = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.star.draw(self.screen)
        pygame.display.flip()
    
    def _create_sky(self):
        star = Star(self)
        margin = 100
        marginX = margin
        marginY = margin
        star_width, star_height = star.rect.size
        number_colums = round(self.setting.screen_width / (marginX + star_width)) - 1
        number_rows = round(self.setting.screen_height / (marginY + star_height)) - 1

        random_number = 10
        count = 0

        for row in range(number_rows):
            for column in range(number_colums):
                drawit = randint(0,1)
                if drawit == 1: 
                    self._create_stars(marginX,marginY)
                    marginX += star_width + margin
                    count += 1
            marginY += star_height + margin
            marginX = margin
            if count == random_number:
                break

    def _create_stars(self, marginX, marginY):
        star = Star(self)
        star.rect.x = marginX
        star.rect.y = marginY
        self.star.add(star)
    
if __name__ == '__main__':
    game = betterStars()
    game.run_game()