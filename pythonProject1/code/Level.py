#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.mode = menu_option  # Opção do menu
        self.name = name

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.cord)
                ent.move()
            pygame.display.flip()
        pass

