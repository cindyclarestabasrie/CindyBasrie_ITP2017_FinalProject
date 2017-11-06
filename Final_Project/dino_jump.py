import pygame.sprite
from Final_Project.settings import Settings
import Final_Project.game_functions as gf
from Final_Project.characters import *
from Final_Project.score import Score
from Final_Project.start import Game_start
import time

def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Dino Jump")
    dino = Dino(screen)
    cactus = Cactus(screen)
    cacti = pygame.sprite.Group(cactus)
    bird = Bird(screen)
    birds = pygame.sprite.Group(bird)
    score = Score(screen, settings)
    start = Game_start(screen)
    game = False

    while True:
        gf.update(screen, score, settings, dino, cacti, birds)
        gf.events(dino)
        if game is False:
            start.blitme()
            if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_SPACE]:
                game = True
        elif game is True:
            # So score increases in number
            score.prep_score()
            score.prep_high_score()

            gf.spawn_new_obstacles(screen, cacti, birds)
            gf.begone_old_obstacles(cacti, birds)

            dino.animated()

            # If dinosaur collides with obstacle, score resets and dinosaur begins again slowly <-- but it still does not work
            if (pygame.sprite.spritecollideany(dino, cacti)) or (pygame.sprite.spritecollideany(dino, birds)):
                time.sleep(1)
                gf.reset(birds, cacti, dino, score)
                print("Collided! Game over!")
                game = False

        pygame.display.flip()

run_game()
