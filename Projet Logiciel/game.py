import pygame
from player import Player

#crere une classe qui represente notre jeu
class Game:
    def __init__(self):
        #generer notre joueur
        self.player = Player()
        self.pressed = {}
        