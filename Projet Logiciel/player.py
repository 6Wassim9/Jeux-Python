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
        self.image = pygame.image.load('Projet Logiciel/images/personnage.png')
        self.newPersonnage = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.newPersonnage.get_rect()
        self.rect.x = 0
        self.rect.y = 180
        
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
    
    def update_health_bar(self):
        #definir une couleur pour notre jauge de vie (verte clair)
        bar_color = (111, 210, 46)
        
        #definir une couleur pour l'arriere plan de jauge (gris foncé)
        back_bar_color = (60,63,60)
        
        #definir la position de notre jauge de vie ainsi que sa largeur et son eppésseur 
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
                
        #definir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 5]
        
        #dessiner notre bar de vie 
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        
    def move_right(self):
         # si le joueur n'est pas en collision avec monstre
        if not self.game.check_collision(self, self.game.all_monsters) :
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity
    