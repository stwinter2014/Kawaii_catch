import pygame

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

