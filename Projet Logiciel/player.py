import pygame
from projectile import Projectile
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100 
        self.max_health = 100 
        self.attack = 10 
        self.velocity = 1 # la vitesse de l'avatar
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('images/personnage.png')
        self.newPersonnage = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.newPersonnage.get_rect()
        self.rect.x = 0
        self.rect.y = 180
    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
    def move_right(self):
        self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity
    