import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.image = pygame.image.load("graphic/player.png")

        self.facing_right = True
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)



    def animate(self):

        image = pygame.image.load("graphic/player.png")
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image




    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.facing_right = True
            self.direction.x = 2
        elif keys[pygame.K_a]:
            self.facing_right = False
            self.direction.x = -2
        else:
            self.direction.x = 0

        if keys[pygame.K_s]:
            self.direction.y = 2
        elif keys[pygame.K_w]:
            self.direction.y = -2
        else:
            self.direction.y = 0



    def update(self):
        self.get_input()
        self.animate()
