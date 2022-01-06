import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphic/wall.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        pass


class Barrel(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphic/barrel.png")
        self.rect = self.image.get_rect(topleft=pos)


class Spot(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("graphic/spot.png")
        self.rect = self.image.get_rect(topleft=pos)
