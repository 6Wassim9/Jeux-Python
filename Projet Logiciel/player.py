import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100 # pa concerné
        self.max_health = 100 # pas concerné 
        self.velocity = 1 # la vitesse de l'avatar
        self.image = pygame.image.load('images/personnage.png')
        self.newPersonnage = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.newPersonnage.get_rect()
        self.rect.x = 0
        self.rect.y = 180
    
    def move_right(self):
        self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity
    
    def move_up(self):
        self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity    