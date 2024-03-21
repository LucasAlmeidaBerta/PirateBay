#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.mode = menu_option  # Opção do menu
        self.name = name
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option == MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)


    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.cord)
                self.level_text(14,f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.screen.blit(source=text_surf, dest=text_rect)
