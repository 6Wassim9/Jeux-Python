import pygame
from game import Game
from player import Player

pygame.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("the fucking maze")
screen = pygame.display.set_mode((1000, 600))

#importer l'arriere plan sur les mesure de la fenetre noir
background = pygame.image.load('images/istockphoto-1305076925-1024x1024.jpg')
newImage = pygame.transform.scale(background, (1000, 600))

#changement du nom de la classe 
game = Game()

#condition de marche vérifiée
running = True

#charger notre joueur
player = Player()

#importer notre baniere 
banner = pygame.image.load('images/istockphoto-1305076925-1024x1024.jpg')

while running :
    
    #appliquer l'arriere plan de notre jeu
    screen.blit(newImage, (0,0))
    
    #appliquer l'image de mon joueur 
    screen.blit(game.player.newPersonnage, game.player.rect)
    
    #vérifier si notre jeu a commencé ou non
    #if game.is_playing:
        #declencher les instructions de la partie
        #game.update(screen)
        
    #verifier que le jeu n'a pas encore commencé
    #else: 
        #ajouter mon ecran de bienvenue
        #screen.blit(banner, (0,0))
    #verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 900:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -5:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > -5:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y< 500:
        game.player.move_down()
    
    
    #mettre a jour l'ecran
    pygame.display.flip()
    
    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'envirenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter si un joueur lache une touche du clavier
        #elif event.type == pygame.KEYDOWN:
            #quelle touche a été utilisée
            #if event.key == pygame.K_RIGHT:
                #game.player.move_right()
            #elif event.key == pygame.K_LEFT:
                #game.player.move_left()
            #elif event.key == pygame.K_UP:
                #game.player.move_up()
            #elif event.key == pygame.K_DOWN:
                #game.player.move_down()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
                
                
                


