import pygame
from pygame.constants import K_ESCAPE
from map import levels_maps, screen_width, game_states


class Menu():
    def __init__(self, surface):
        self.dispaly = surface
        self.font = pygame.font.Font("graphic/Bombing.ttf", 50)
        self.image = pygame.Surface((48, 48))
        self.image.fill("#009966")
        self.level_index = 0


class InitialMenu(Menu):
    def __init__(self, surface):
        super().__init__(surface)

    def initial_menu(self):

        """
        Displays the button "Play"
        """

        self.initial = self.font.render("Play", False, (64, 64, 64))
        self.play_ag_rect = self.initial.get_rect(center=(screen_width/2, 150))

        mouse = pygame.mouse.get_pos()
        if self.play_ag_rect.collidepoint(mouse):
            pygame.draw.rect(self.dispaly, "#009966", self.play_ag_rect)
            pygame.draw.rect(self.dispaly, "#009966", self.play_ag_rect, 10)
        else:
            pygame.draw.rect(self.dispaly, "#33ffbb", self.play_ag_rect)
            pygame.draw.rect(self.dispaly, "#33ffbb", self.play_ag_rect, 10)
        self.dispaly.blit(self.initial, self.play_ag_rect)

    def game_status(self):
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_ag_rect.collidepoint(mouse) and mouse_button[0]:
            return game_states["run"]
        return game_states["init"]

    def run(self):
        self.initial_menu()
        self.game_status()


class MenuNextLevel(Menu):
    def __init__(self, surface):
        super().__init__(surface)

    def play_again(self):

        """
        Displays the button "Play Again"
        """

        self.play_ag = self.font.render("Play Again", False, (64, 64, 64))
        self.play_ag_rect = self.play_ag.get_rect(center=(screen_width/2, 250))

        mouse = pygame.mouse.get_pos()
        if self.play_ag_rect.collidepoint(mouse):
            pygame.draw.rect(self.dispaly, "#009966", self.play_ag_rect)
            pygame.draw.rect(self.dispaly, "#009966", self.play_ag_rect, 10)
        else:
            pygame.draw.rect(self.dispaly, "#33ffbb", self.play_ag_rect)
            pygame.draw.rect(self.dispaly, "#33ffbb", self.play_ag_rect, 10)
        self.dispaly.blit(self.play_ag, self.play_ag_rect)

    def next_level(self):

        """
        Displays the button "Next Level"
        """

        self.next = self.font.render("Next Level", True, (64, 64, 64))
        self.next_rect = self.next.get_rect(center=(screen_width/2, 150))

        mouse = pygame.mouse.get_pos()
        if self.next_rect.collidepoint(mouse):
            pygame.draw.rect(self.dispaly, "#009966", self.next_rect)
            pygame.draw.rect(self.dispaly, "#009966", self.next_rect, 10)
        else:
            pygame.draw.rect(self.dispaly, "#33ffbb", self.next_rect)
            pygame.draw.rect(self.dispaly, "#33ffbb", self.next_rect, 10)
        self.dispaly.blit(self.next, self.next_rect)

    def game_status(self):
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.play_ag_rect.collidepoint(mouse) and mouse_button[0]:
            return game_states["run"]
        if self.next_rect.collidepoint(mouse) and mouse_button[0]:
            return game_states["run"]
        return game_states["main"]

    def level_counter(self):

        """
        Count the curren level index
        """

        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.next_rect.collidepoint(mouse) and mouse_button[0]:
            self.level_index += 1
            if self.level_index >= len(levels_maps):
                self.level_index = 0

    def open_menu(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return game_states["restart"]
        return game_states["run"]

    def run(self):
        self.play_again()
        self.next_level()
        self.level_counter()


class RestartMenu(Menu):

    def __init__(self, surface):
        super().__init__(surface)

    def restart(self):

        """
        Displays the button "Restart"
        """

        self.rest = self.font.render("Restart", False, (64, 64, 64))
        self.rest_rect = self.rest.get_rect(center=(screen_width/2, 150))

        mouse = pygame.mouse.get_pos()
        if self.rest_rect.collidepoint(mouse):
            pygame.draw.rect(self.dispaly, "#009966", self.rest_rect)
            pygame.draw.rect(self.dispaly, "#009966", self.rest_rect, 10)
        else:
            pygame.draw.rect(self.dispaly, "#33ffbb", self.rest_rect)
            pygame.draw.rect(self.dispaly, "#33ffbb", self.rest_rect, 10)
        self.dispaly.blit(self.rest, self.rest_rect)

    def continue_game(self):

        """
        Displays the button "Continue"
        """

        self.cont = self.font.render("Continue", False, (64, 64, 64))
        self.cont_rect = self.cont.get_rect(center=(screen_width/2, 250))

        mouse = pygame.mouse.get_pos()
        if self.cont_rect.collidepoint(mouse):
            pygame.draw.rect(self.dispaly, "#009966", self.cont_rect)
            pygame.draw.rect(self.dispaly, "#009966", self.cont_rect, 10)
        else:
            pygame.draw.rect(self.dispaly, "#33ffbb", self.cont_rect)
            pygame.draw.rect(self.dispaly, "#33ffbb", self.cont_rect, 10)
        self.dispaly.blit(self.cont, self.cont_rect)

    def game_restart(self):
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.rest_rect.collidepoint(mouse) and mouse_button[0]:
            return game_states["run"]
        return game_states["restart"]

    def game_continue(self):
        mouse = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()
        if self.cont_rect.collidepoint(mouse) and mouse_button[0]:
            return game_states["run"]
        return game_states["restart"]

    def run(self):
        self.restart()
        self.continue_game()
