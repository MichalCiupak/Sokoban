import pygame
from map import screen_width
from menu import Menu, InitialMenu, MenuNextLevel, RestartMenu
pygame.font.init()
screen = pygame.display.set_mode((screen_width, 1000))


def test_create_menu():
    menu = Menu(screen)
    assert menu


def test_create_initialmenu():
    menu = InitialMenu(screen)
    assert menu


def test_create_nextlevelmenu():
    menu = MenuNextLevel(screen)
    assert menu


def test_create_restartmenu():
    menu = RestartMenu(screen)
    assert menu


def test_menunextlevel_position():
    menu = MenuNextLevel(screen)
    menu.play_again()
    menu.next_level()
    assert menu.play_ag_rect.center == (screen_width/2, 250)
    assert menu.next_rect.center == (screen_width/2, 150)


def test_restartmenu_position():
    menu = RestartMenu(screen)
    menu.restart()
    menu.continue_game()
    assert menu.rest_rect.center == (screen_width/2, 150)
    assert menu.cont_rect.center == (screen_width/2, 250)


def test_restartmenu_functions():
    menu = RestartMenu(screen)
    menu.run()
    assert menu.game_restart() == "restartmenu"
    assert menu.game_continue() == "restartmenu"


def test_menunextlevel_functions():
    menu = MenuNextLevel(screen)
    menu.run()
    assert menu.game_status() == "mainmenu"
    assert menu.open_menu() == "running"


def test_initialmenu_functions():
    menu = InitialMenu(screen)
    menu.run()
    assert menu.game_status() == "initialmenu"
