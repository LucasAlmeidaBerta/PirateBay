#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Background import Background
from code.Const import SCREEN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (SCREEN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, 200))
            case 'Player2':
                return Player('Player2', (100, 210))
            case 'Enemy1':
                return Enemy('Enemy1', (500, 250))