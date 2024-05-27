import pygame 


# creer une classe qui va gerer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite) :

    def __init__(self,game) :
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect( )
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 4
        
    def damage(self, amount) #amount c'est le montant de dégat fait par le montre
        # Infliger les degats
        self.health = amount
    
    def update_health_bar(self):
        #definir une couleur pour notre jauge de vie (verte clair)
        bar_color = (111, 210, 46)
        
        #definir une couleur pour l'arriere plan de jauge (gris foncé)
        back_bar_color = (60,63,60)
        
        #definir la position de notre jauge de vie ainsi que sa largeur et son eppésseur 
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
                
        #definir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        
        #dessiner notre bar de vie 
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        


    def forward(self):
        # le deplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self,self.game.all_players) :
           self.rect.x -= self.velocity



