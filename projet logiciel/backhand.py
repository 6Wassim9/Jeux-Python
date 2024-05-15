import pygame # type: ignore
pygame.init()

#generer la fenetre de notre jeu

pygame.display.set_caption("the fucking maze")
screen = pygame.display.set_mode((1000, 700))

running = True

#boucle en tant que cette condition est vraie 
background = pygame.image.load('images/imaagebackhand.jpg')
while running :
    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0,0))

    #mettre a jour l'ecran
    pygame.display.flip()
    #si le joueur ferme cette fenetre

    for event in pygame.event.get() :

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")




