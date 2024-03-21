#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT
from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.cord.right < 500: # Quando pressionada a tecla seta pra cima
            self.cord.centerx += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.cord.left > 0: # Quando pressionada a tecla seta pra cima
            self.cord.centerx -= ENTITY_SPEED[self.name]


