import pygame.font

class Score:
    """ I referenced the score from python crash course alien invasion """
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 38)
        self.score = 0
        self.high_score = 0
        self.prep_high_score()
        self.prep_score()

    def prep_score(self):
        # Score adds 1/100
        self.score += self.settings.score_add

        # Score is rounded to integer
        self.score_image = self.font.render(str(int(round(self.score, 0))), True, (0, 0, 0))
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.top = self.screen_rect.top
        self.score_image_rect.right = self.screen_rect.right

    def prep_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score

        self.highscore = self.font.render("High Score " + str(int(round(self.high_score, 0))), True, (0, 0, 0))
        self.hs_rect = self.highscore.get_rect()

        self.hs_rect.top = self.screen_rect.top
        self.hs_rect.left = self.screen_rect.left

    def blitme(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highscore, self.hs_rect)
