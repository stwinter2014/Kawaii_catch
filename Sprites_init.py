import pygame
import random
pygame.init()
size = [390, 730]
white = [255, 255, 255]

class Claw (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Claw.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

class Pong_green(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong1_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
class Pong_blue(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong2_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
class Pong_red(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong3_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
class Pong_yellow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong4_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
class Pong_brown(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong5_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
class Pong_purple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong6_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1

class Pong_weapon_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong1_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
class Pong_weapon_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong2_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
class Pong_weapon_3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong3_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
class Pong_weapon_4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong4_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
class Pong_weapon_5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong5_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
class Pong_weapon_6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong6_1.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
