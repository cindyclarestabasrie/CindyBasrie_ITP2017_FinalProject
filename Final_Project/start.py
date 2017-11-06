import pygame.font

class Game_start:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(None, 30)

        self.prep_start()

    def prep_start(self):
        self.start = "Press space or up to start"
        self.image = self.font.render(self.start, True, (50, 50, 50))
        self.image_rect = self.image.get_rect()

        self.image_rect.bottom = self.screen_rect.bottom
        self.image_rect.left = self.screen_rect.left

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
