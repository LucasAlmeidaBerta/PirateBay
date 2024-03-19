#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Const import SCREEN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.cord.centerx -= ENTITY_SPEED[self.name]
        if self.cord.right <= 0:
            self.cord.left = SCREEN_WIDTH
