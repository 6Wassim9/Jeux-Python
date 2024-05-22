import pygame

#creer une premiere classe qui va representer le joueur
class personnage(pygame.sprite.Sprite) :

    def _init_(self) :
        super()._init_()
        self.time =180
        self.max_time =180
        self.deplacement = 200
        self.velocity = 5
        self.image = pygame.image.load('projet logiciel/personnage1.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 1000

#generer la fenetre de notre jeu

    pygame.display.set_caption("the Labyrinth")
screen = pygame.display.set_mode((3500,4000))


#creer une seconde classe qui va representer notre jeu
class Game :

    def _init_(self) :
       #generer notre joueur
       self.personnage =personnage 