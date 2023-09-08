import sys
import pygame
from settings import Settings
from star import Star

class GridStars:

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
        pygame.display.set_caption("Sky full of stars")

        #self.star = Star(self)
        self.star = pygame.sprite.Group()

        self._create_sky()

    def run_game(self):
        while True:
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.star.draw(self.screen)
        pygame.display.flip()

    def _create_sky(self):
        star = Star(self)
        margin = 10
        marginX = margin
        marginY = margin
        star_width, star_height = star.rect.size 
        number_columns = round(self.setting.screen_width / (marginX + star_width)) -1
        number_rows = round(self.setting.screen_height / (marginY + star_height)) - 1

        for row in range(number_rows):
            for columns in range(number_columns):
                self._create_stars(marginX,marginY)
                marginX += star_width + margin
            marginY += star_height + margin
            marginX = margin

        
            
            

    def _create_stars(self,marginX,marginY):
        star = Star(self)
        star.rect.x = marginX
        star.rect.y = marginY
        self.star.add(star)
        

    """ def _create_stars(self,star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = 5 * star_number + star_width
        star.rect.x = star.x
        star.rect.y = row_number + 20 + star_height
        self.star.add(star) """

if __name__ == '__main__':
    #Make a game instance, and run the game 
    ai = GridStars()
    ai.run_game()
