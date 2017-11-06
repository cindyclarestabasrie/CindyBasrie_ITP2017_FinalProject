from pygame.sprite import Sprite
import pygame
import random


class Dino(Sprite):
    """ Dinosaur sprite image taken from
        https://community.playstarbound.com/threads/biped-dinosaur-smaller-dino-egg-bonus-female-duck.110547/"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # List of Dinosaur pictures to look like it is walking
        self.images = [pygame.image.load("dino-sprite-2.png"), pygame.image.load("dino-sprite-3.png"),
                       pygame.image.load("dino-sprite-2.png"), pygame.image.load("dino-sprite-4.png")]

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Position of Dinosaur
        self.rect.x = 30
        # 100 pixels because 20 picels for the green ground and 80 pixels for the dinosaur image height
        self.rect.y = self.screen_rect.bottom - 100

        # Jump movement
        self.jump = False

    def Jump(self):
        # Dinosaur will jump
        if self.jump and self.rect.y > 20:
            self.rect.y -= 3
        # if rect position is less than 21 pixels, it will fall.
        elif self.rect.y < 21:
            self.jump = False

    def Gravity(self):
        # Dinosaur will fall back to original position on the ground
        if self.jump is False and self.rect.y < self.screen_rect.bottom - 100:
            self.rect.y += 1


    def animated(self):
        """ Michael0x2a. Retrieved from: https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images """
        # Make Dinosaur looks like it is running
        # if index is less than 3, it will add 1
        if self.index < (len(self.images) - 1):
            self.index += 1
            self.image = self.images[self.index]
        # if index is 3, it will return back to 0
        elif self.index == (len(self.images) - 1):
            self.index = 0
            self.image = self.images[self.index]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Cactus(Sprite):
    """ Picture of Cactus taken from
    https://i.pinimg.com/236x/44/d2/e2/44d2e202c4c508417576d0db73d604b4--fantasy-series-final-fantasy.jpg"""
    def __init__(self, screen):
        super(Cactus, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # Loading Cactus images
        individual = pygame.image.load("mintuarr.png")
        many = pygame.image.load("minutuars.png")

        # List of cactus images
        self.images = [pygame.transform.scale(individual, (100, 100)), individual,
                       pygame.transform.flip(many, True, True), many]

        # Random cactus image from list will appear everytime new cactus spawna
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()

        # Where cactus will spawn
        self.rect.bottom = self.screen_rect.bottom - 20
        self.rect.x = self.screen_rect.right + 140 + random.randint(-100, 800)

    def moving(self):
        # Cactus will move towards the left side of screen
        self.rect.x -= 3

class Bird(Sprite):
    """ Picture of bird taken from
    https://www.shutterstock.com/image-illustration/flying-bird-animation-pixel-art-646008130?src=F0hVLqnJ7uXJv7oMOjrXLA-1-40"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.images = [pygame.image.load("bird1.png"), pygame.image.load("bird2.png"),
                       pygame.image.load("bird3.png"), pygame.image.load("bird4.png"),
                       pygame.image.load("bird3.png"), pygame.image.load("bird2.png")]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # The heights it will be appearing in
        self.positions = [20, 100, 180]
        self.rect.y = random.choice(self.positions)

        # Bird will spawn somewhere off the screen
        self.rect.x = self.screen_rect.right + random.randint(800, 5000)


    def animated(self):
        # Bird will look like flapping its wings
        if self.index < (len(self.images) - 1):
            self.counter += 1

        if self.counter == 10:
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]
        elif self.index == (len(self.images) - 1):
            self.index = 0
            self.image = self.images[self.index]


    def moving(self):
        # Bird moves towards the left side of screen
        self.rect.x -= 4
