import pygame
import json
from elements import Tile, Barrel
from player import Player
from map import Map
pygame.mixer.init()

with open("levels.json", "r") as file_handle:
    data = json.load(file_handle)

levels_maps = []
for value in data.values():
    levels_maps.append(value)

element_size = 64
screen_height = element_size*7
screen_width = element_size*13
screen = pygame.display.set_mode((screen_width, screen_height))
map = Map(levels_maps, screen)


def test_reading_from_file():
    assert len(levels_maps) == 5


def test_crate_map():
    map = Map(levels_maps, screen)
    assert map


def test_setup_level():
    map = Map(levels_maps, screen)
    map.setup_level(levels_maps)
    assert type(map.spots) == pygame.sprite.Group
    assert type(map.barrels) == pygame.sprite.Group
    assert type(map.tiles) == pygame.sprite.Group
    assert type(map.player) == pygame.sprite.GroupSingle


def test_barrels_on_spot():
    map = Map(levels_maps[0], screen)
    map.setup_level(levels_maps[0])
    status = map.barrels_on_spot()
    assert status == "running"


def test_x_collision_wall():
    map = Map(levels_maps[0], screen)
    map.setup_level(levels_maps[0])
    tile = Tile((1, 1))
    map.tiles.add(tile)
    player = Player((1, 1))
    map.player.add(player)
    player.direction.x = 2
    assert map.player.sprite.rect.topleft == (1, 1)
    map.x_collision_wall()
    assert map.player.sprite.rect.topleft == (-29, 1)


def test_y_collision_wall():
    map = Map(levels_maps[0], screen)
    map.setup_level(levels_maps[0])
    tile = Tile((1, 1))
    map.tiles.add(tile)
    player = Player((1, 1))
    map.player.add(player)
    player.direction.y = 2
    assert map.player.sprite.rect.topleft == (1, 1)
    map.y_collision_wall()
    assert map.player.sprite.rect.topleft == (1, -51)


def test_y_collison_barrel():
    map = Map(levels_maps[0], screen)
    map.setup_level(levels_maps[0])
    tile = Tile((1, 1))
    map.tiles.add(tile)
    player = Player((1, 1))
    barrel = Barrel((1, 1))
    map.barrels.add(barrel)
    map.player.add(player)
    assert map.player.sprite.rect.topleft == (1, 1)
    player.direction.y = 2
    map.y_collision_barrel()
    assert map.player.sprite.rect.topleft == (1, -114)


def test_x_collison_barrel():
    map = Map(levels_maps[0], screen)
    map.setup_level(levels_maps[0])
    tile = Tile((1, 1))
    map.tiles.add(tile)
    player = Player((1, 1))
    barrel = Barrel((1, 1))
    map.barrels.add(barrel)
    map.player.add(player)
    assert map.player.sprite.rect.topleft == (1, 1)
    player.direction.x = 2
    map.x_collision_barrel()
    assert map.player.sprite.rect.topleft == (-93, 1)
