import pygame
from sys import exit
from levels import *
from map import Map, element_size
from menu import Menu, RestartMenu, MenuNextLevel, InitialMenu


pygame.init()
pygame.display.set_caption("Sokoban")


screen_height = tile_size*7
screen_width = tile_size*13

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Map(levels_maps[0],screen)


menu = Menu(screen)
restart_menu = RestartMenu(screen)
next_level_menu = MenuNextLevel(screen)
initial_menu = InitialMenu(screen)
game_status = "initialmenu"


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_status == "initialmenu":
        initial_menu.run()
        game_status = initial_menu.game_status()

    elif game_status == "running":
        screen.fill("#E7D36E")
        level.run()
        if next_level_menu.open_menu() == "restartmenu":
            game_status = "restartmenu"
            continue
        game_status = level.barrels_on_spot()

    elif game_status == "mainmenu":
        next_level_menu.run()
        game_status = next_level_menu.game_status()
        level = Map(levels_maps[next_level_menu.level_index],screen)

    elif game_status == "restartmenu":
        restart_menu.run()
        if restart_menu.game_restart() == "running":
            game_status = "running"
            level = Map(levels_maps[next_level_menu.level_index],screen)
        if restart_menu.game_continue() == "running":
            game_status = "running"


    pygame.display.update()
    clock.tick(60)
