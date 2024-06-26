import pygame

#definir la classe qui va gérer le projectile de notre joueur 
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('images/pngtree-projectile-explosion-icon-in-flat-circle-isolated-on-white-background-vector-illustration-for-web-picture-image_8063331.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect() 
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0
        self.player = player
        
    def damage(amount):
        self.health -= amount 

    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        #tourner le projectile
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move (self):
        self.rect.x += self.velocity
        self.rotate()
        
        #vérifier si le projectile entre en collision avec un monstre // NORMALEMT NTOUMA LI DIROUH MAIS ANI DERTOU F PLASSETKOOUM
        for monster in  self.player.game.check_collaision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.recmove()
            #infliger des dégats
            monster.damage(self.player.attack)
        
        #verifier si notre projectile n'est plus présent sur l'écran
        for montre in self.rect.x > 1080:
            
            #supprimer le projectile (en dehors de l'ecran)
            self.remove()
