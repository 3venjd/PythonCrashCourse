import pygame

class palace:

    def __init__(self, gCharacter):
        self.screen = gCharacter.screen
        self.screen_rect = gCharacter.screen.get_rect()

        self.image = pygame.image.load("Chapter_12\\Excersice_12_2\\Images\\floatingPalace.bmp")
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (60,60))
        self.image_position = (gCharacter.settings.screen_witdh/2,gCharacter.settings.screen_heigth/2)

    def blitme(self):
        self.screen.blit(self.image, self.image_position)