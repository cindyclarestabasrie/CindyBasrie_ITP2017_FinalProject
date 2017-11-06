import pygame
import sys
from Final_Project.characters import *

def events(dino):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, dino)

def keydown_events(event, dino):
    """ Make the Dinosaur jump and fall when key is pressed. """
    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        # if rect position is more than 190 pixels, the dinosaur is able to jump
        if dino.rect.y > 190:
            dino.jump = True
            jump = pygame.mixer.SoundType("jump.wav")
            pygame.mixer.Sound.play(jump)

# New Obstacles will be added if old one is removed
def spawn_new_obstacles(screen, cacti, birds):
    cactus = Cactus(screen)
    if len(cacti) < 1:
        cacti.add(cactus)
    bird = Bird(screen)
    if len(birds) < 1:
        birds.add(bird)

# Removes old obstacles that the dinosaur has passed
def begone_old_obstacles(cacti, birds):
    for cactus in cacti:
        cactus.moving()
        if cactus.rect.x < -140:
            cacti.remove(cactus)
    for bird in birds:
        bird.moving()
        bird.animated()
        if bird.rect.x < -60:
            birds.remove(bird)

# Resets speed and score
def reset(birds, cacti, dino, score):
    birds.empty()
    cacti.empty()
    score.score = 0
    dino.rect.y = dino.screen_rect.bottom - 100

# Update the screen according to events
def update(screen, score, settings, dino, cacti, birds):
    screen.fill(settings.bg_color)
    score.blitme()
    dino.Jump()
    dino.Gravity()
    # Characters on screen
    dino.blitme()
    cacti.draw(screen)
    birds.draw(screen)
    # The green ground
    pygame.draw.rect(screen, (0, 236, 120), (0, settings.screen_height - 20, settings.screen_width, 20))


