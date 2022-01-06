import pygame
from pygame.constants import K_ESCAPE
from levels import *

class Menu():
    def __init__(self, surface):
        self.display_surface = surface
        self.font = pygame.font.Font("graphic/Bombing.ttf", 50)
        self.image = pygame.Surface((48,48))
        self.image.fill("#009966")
        self.level_index = 0


class InitialMenu(Menu):
    def __init__(self, surface):
        super().__init__(surface)


    def initial_menu(self):
        self.play_initial_text = self.font.render(f"Play", False, (64, 64, 64))
        self.play_again_text_rect = self.play_initial_text.get_rect(center = (screen_width/2, 150))

        mouse =pygame.mouse.get_pos()
        if self.play_again_text_rect.collidepoint(mouse):
            pygame.draw.rect(self.display_surface, "#009966", self.play_again_text_rect)
            pygame.draw.rect(self.display_surface, "#009966", self.play_again_text_rect, 10)
        else:
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_again_text_rect)
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_again_text_rect, 10)
        self.display_surface.blit(self.play_initial_text, self.play_again_text_rect)


    def game_status(self):
        mouse =pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_again_text_rect.collidepoint(mouse) and mouse_button[0]:
            return "running"
        return "initialmenu"


    def run(self):
        self.initial_menu()
        self.game_status()


class MenuNextLevel(Menu):
    def __init__(self, surface):
        super().__init__(surface)


    def play_again(self):
        self.play_again_text = self.font.render(f"Play Again", False, (64, 64, 64))
        self.play_again_text_rect = self.play_again_text.get_rect(center = (screen_width/2, 250))

        mouse =pygame.mouse.get_pos()
        if self.play_again_text_rect.collidepoint(mouse):
            pygame.draw.rect(self.display_surface, "#009966", self.play_again_text_rect)
            pygame.draw.rect(self.display_surface, "#009966", self.play_again_text_rect, 10)
        else:
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_again_text_rect)
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_again_text_rect, 10)
        self.display_surface.blit(self.play_again_text, self.play_again_text_rect)


    def next_level(self):
        self.play_next_text = self.font.render(f"Next Level", True, (64, 64, 64))
        self.play_next_text_rect = self.play_next_text.get_rect(center = (screen_width/2, 150))

        mouse =pygame.mouse.get_pos()
        if self.play_next_text_rect.collidepoint(mouse):
            pygame.draw.rect(self.display_surface, "#009966", self.play_next_text_rect)
            pygame.draw.rect(self.display_surface, "#009966", self.play_next_text_rect, 10)
        else:
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_next_text_rect)
            pygame.draw.rect(self.display_surface, "#33ffbb", self.play_next_text_rect, 10)
        self.display_surface.blit(self.play_next_text, self.play_next_text_rect)


    def game_status(self):
        mouse =pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_again_text_rect.collidepoint(mouse) and mouse_button[0]:
            return "running"
        if self.play_next_text_rect.collidepoint(mouse) and mouse_button[0]:
            return "running"
        return "mainmenu"


    def level_counter(self):
        mouse =pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_next_text_rect.collidepoint(mouse) and mouse_button[0]:
            self.level_index += 1
            if self.level_index >= len(levels_maps):
                self.level_index = 0


    def open_menu(self):
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return "restartmenu"
        return "running"


    def run(self):
        self.play_again()
        self.next_level()
        self.level_counter()

class RestartMenu(Menu):
    def __init__(self, surface):
        super().__init__(surface)


    def restart(self):
        self.play_restart_text = self.font.render(f"Restart",False,(64,64,64))
        self.play_restart_text_rect = self.play_restart_text.get_rect(center = (screen_width/2,150))

        mouse =pygame.mouse.get_pos()
        if self.play_restart_text_rect.collidepoint(mouse):
            pygame.draw.rect(self.display_surface,"#009966",self.play_restart_text_rect)
            pygame.draw.rect(self.display_surface,"#009966",self.play_restart_text_rect,10)
        else:
            pygame.draw.rect(self.display_surface,"#33ffbb",self.play_restart_text_rect)
            pygame.draw.rect(self.display_surface,"#33ffbb",self.play_restart_text_rect,10)
        self.display_surface.blit(self.play_restart_text,self.play_restart_text_rect)

    def continue_game(self):
        self.play_continue_text = self.font.render(f"Continue",False,(64,64,64))
        self.play_continue_text_rect = self.play_continue_text.get_rect(center = (screen_width/2,250))

        mouse =pygame.mouse.get_pos()
        if self.play_continue_text_rect.collidepoint(mouse):
            pygame.draw.rect(self.display_surface,"#009966",self.play_continue_text_rect)
            pygame.draw.rect(self.display_surface,"#009966",self.play_continue_text_rect,10)
        else:
            pygame.draw.rect(self.display_surface,"#33ffbb",self.play_continue_text_rect)
            pygame.draw.rect(self.display_surface,"#33ffbb",self.play_continue_text_rect,10)
        self.display_surface.blit(self.play_continue_text,self.play_continue_text_rect)

    def game_restart(self):
        mouse =pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_restart_text_rect.collidepoint(mouse) and mouse_button[0]:
            return "running"
        return "restartmenu"

    def game_continue(self):
        mouse =pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_continue_text_rect.collidepoint(mouse) and mouse_button[0]:
            return "running"
        return "restartmenu"
    def run(self):
        self.restart()
        self.continue_game()

