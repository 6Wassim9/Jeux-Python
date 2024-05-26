import pygame

#definir la classe qui va gérer le projectile de notre joueur 
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('images/pngtree-projectile-explosion-icon-in-flat-circle-isolated-on-white-background-vector-illustration-for-web-picture-image_8063331.png')
        self.rect = self.image.get_rect() 
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
    def move (self):
        self.rect.x += self.velocity
        self.rotate()
        #verifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1000:

            #supprimer le projectile (en dehors de l'ecran)
            self.player.all_projectiles.remove(self)
