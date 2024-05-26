import pygame

#definir la classe qui va gérer le projectile de notre joueur 
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('images/pngtree-projectile-explosion-icon-in-flat-circle-isolated-on-white-background-vector-illustration-for-web-picture-image_8063331.png')
        self.rect = self.image.get_rect() 
        