import pygame
from sys import exit
from map import Map, screen_height, screen_width, levels_maps, game_states
from menu import RestartMenu, MenuNextLevel, InitialMenu


def main():
    pygame.init()
    pygame.display.set_caption("Sokoban")

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    level = Map(levels_maps[0], screen)

    restart_menu = RestartMenu(screen)
    next_level_menu = MenuNextLevel(screen)
    initial_menu = InitialMenu(screen)
    game_status = game_states["init"]


# Main loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_status == game_states["init"]:
            initial_menu.run()
            game_status = initial_menu.game_status()

        elif game_status == game_states["run"]:
            bg_color = "#E7D36E"
            screen.fill(bg_color)
            level.run()
            if next_level_menu.open_menu() == game_states["restart"]:
                game_status = game_states["restart"]
                continue
            game_status = level.barrels_on_spot()

        elif game_status == game_states["main"]:
            next_level_menu.run()
            game_status = next_level_menu.game_status()
            level = Map(levels_maps[next_level_menu.level_index], screen)

        elif game_status == game_states["restart"]:
            restart_menu.run()
            if restart_menu.game_restart() == game_states["run"]:
                game_status = game_states["run"]
                level = Map(levels_maps[next_level_menu.level_index], screen)
            if restart_menu.game_continue() == game_states["run"]:
                game_status = game_states["run"]

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
