#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCREEN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)
    def run(self):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:

            # Desenhar na tela

            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Pirate",COLOR_ORANGE,(SCREEN_WIDTH / 2, 70))
            self.menu_text(50, "Bay", COLOR_ORANGE, (SCREEN_WIDTH / 2, 120))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (SCREEN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (SCREEN_WIDTH / 2, 200 + 30 * i))

            # Verificar eventos

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # se a tecla seta para baixo for pressionada
                        menu_option += 1
                        if menu_option > 2:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # se a tecla seta para cima for pressionada
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = 2
                    if event.key == pygame.K_RETURN:  # se a tecla enter for pressionada
                        return MENU_OPTION[menu_option]
            pygame.display.flip()
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)

