import pygame
from player import Player

#crere une classe qui represente notre jeu
class Game:
    def __init__(self):
        #definir si notre jeu à commencer ou non
        self.is_playing = False
        
        #generer notre joueur
        self.player = Player()
        self.pressed = {}
    
    def update(self, screen):
        #appliquer l'image de mon joueur 
        screen.blit(self.player.newPersonnage, self.player.rect)
        
        #vérifier si notre jeu a commencé ou non
        
        #verifier si le joueur souhaite aller a gauche ou a droite ou en haut ou en bas
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 900:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -5:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > -5:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y< 500:
            self.player.move_down()
