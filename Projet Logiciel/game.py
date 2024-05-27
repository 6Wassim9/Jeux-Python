import pygame
from player import Player
from monster import Monster

#crere une classe qui represente notre jeu
class Game:
    def __init__(self):
        #definir si notre jeu à commencer ou non
        self.is_playing = False
        
        #generer notre joueur
        self.player = Player()
        self.pressed = {}
        
        #groupe de monstres
        self.all_monstres = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
    
    def update(self, screen):
        
        #appliquer l'image de mon joueur 
        screen.blit(self.player.newPersonnage, self.player.rect)
        
        #récuperer les projectiles du joueur 
        for projectile in self.player.all_projectiles:
            projectile.move()
            
        #recuperer les monstres de notre jeau //HADI NORMALEMEN NTOU DIROUHA MAIS NSSAHA9 NZID NDIR FIHA DONC NI DERTHA
        for monster in game.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            
            
        #appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)
    
        #verifier si le joueur souhaite aller a gauche ou a droite ou en haut ou en bas
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 900:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -5:
            self.player.move_left()
            
def spawn_monster(self):
    monster = Monster()
    self.all_monster.add(monster)
