import pygame
import json
from elements import Tile, Barrel, Spot
from player import Player

with open("levels.json", "r") as file_handle:
    data = json.load(file_handle)

levels_maps = []
for value in data.values():
    levels_maps.append(value)

element_size = 64
screen_height = element_size*7
screen_width = element_size*13


class Map():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.push = pygame.mixer.Sound("graphic/push.wav")

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.barrels = pygame.sprite.Group()
        self.spots = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "X":
                    x = col_index*element_size
                    y = row_index*element_size
                    tile = Tile((x, y))
                    self.tiles.add(tile)
                if cell == "@":
                    x = col_index*element_size
                    y = row_index*element_size
                    player = Player((x, y))
                    self.player.add(player)
                if cell == "B":
                    x = col_index*element_size
                    y = row_index*element_size
                    barrel = Barrel((x, y))
                    self.barrels.add(barrel)
                if cell == "S":
                    x = col_index*element_size
                    y = row_index*element_size
                    spot = Spot((x, y))
                    self.spots.add(spot)

    def x_collision_wall(self):
        player = self.player.sprite
        player.rect.x += player.direction.x
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def x_collision_barrel(self):
        player = self.player.sprite
        for sprite in self.barrels.sprites():
            if sprite.rect.colliderect(player.rect):
                position = sprite.rect.right
                sprite.rect.right += 32*player.direction.x
                for other_sprite in self.tiles.sprites():
                    if sprite.rect.colliderect(other_sprite.rect):
                        if player.direction.x < 0:
                            sprite.rect.left = other_sprite.rect.right
                            player.rect.left = sprite.rect.right
                        if player.direction.x > 0:
                            sprite.rect.right = other_sprite.rect.left
                            player.rect.right = sprite.rect.left
                for other_sprite in self.barrels.sprites():
                    if sprite == other_sprite:
                        continue
                    if sprite.rect.colliderect(other_sprite.rect):
                        if player.direction.x < 0:
                            sprite.rect.left = other_sprite.rect.right
                            player.rect.left = sprite.rect.right
                        if player.direction.x > 0:
                            sprite.rect.right = other_sprite.rect.left
                            player.rect.right = sprite.rect.left
                if not position == sprite.rect.right:
                    self.push.play()

    def y_collision_barrel(self):
        player = self.player.sprite
        for sprite in self.barrels.sprites():
            if sprite.rect.colliderect(player.rect):
                position = sprite.rect.bottom
                sprite.rect.bottom += 32*player.direction.y
                for other_sprite in self.tiles.sprites():
                    if sprite.rect.colliderect(other_sprite.rect):
                        if player.direction.y < 0:
                            sprite.rect.top = other_sprite.rect.bottom
                            player.rect.top = sprite.rect.bottom
                        if player.direction.y > 0:
                            sprite.rect.bottom = other_sprite.rect.top
                            player.rect.bottom = sprite.rect.top
                for other_sprite in self.barrels.sprites():
                    if sprite == other_sprite:
                        continue
                    if sprite.rect.colliderect(other_sprite.rect):
                        if player.direction.y < 0:
                            sprite.rect.top = other_sprite.rect.bottom
                            player.rect.top = sprite.rect.bottom
                        if player.direction.y > 0:
                            sprite.rect.bottom = other_sprite.rect.top
                            player.rect.bottom = sprite.rect.top
                if not position == sprite.rect.bottom:
                    self.push.play()

    def y_collision_wall(self):
        player = self.player.sprite
        player.rect.y += player.direction.y
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

    def barrels_on_spot(self):
        counter = 0
        for sprite in self.barrels.sprites():
            for other_sprite in self.spots.sprites():
                if other_sprite.rect.colliderect(sprite.rect):
                    counter += 1
        if counter == len(self.barrels):
            return "mainmenu"
        return "running"

    def run(self):
        self.player.update()
        self.x_collision_wall()
        self.x_collision_barrel()
        self.y_collision_wall()
        self.y_collision_barrel()
        self.tiles.draw(self.display_surface)
        self.spots.draw(self.display_surface)
        self.barrels.draw(self.display_surface)
        self.player.draw(self.display_surface)
