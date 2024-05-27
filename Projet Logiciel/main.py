import pygame
import math
from game import Game
from player import Player

#coucou c'est le pc de Wassim TEST TEST TEST





pygame.init()

#generer la fenetre de notre jeu
pygame.display.set_caption("the fucking maze")
screen = pygame.display.set_mode((1000, 600))

#importer l'arriere plan sur les mesure de la fenetre noir
background = pygame.image.load('images/istockphoto-1305076925-1024x1024.jpg')
newImage = pygame.transform.scale(background, (1000, 600))

#importer notre baniere
banner = pygame.image.load('images/banner.png') #il faut que ça soint en .png car il faut avoir une transparansse
banner = pygame.transform.scale(banner,(500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4) #centraliser l'ecran d'acceuil

#importer notre bouton pour lancer la partie
play_button = pygame.image.load('images/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33) #centraliser le play button sur l'axe x
play_button_rect.y = math.ceil(screen.get_height()/2) #centraliser le play button sur l'axe y
                    #### remrque in peut inversser les 2 dernieres ligne pour avoir le bouton deriere le logo

#changement du nom de la classe 
game = Game()

#condition de marche vérifiée
running = True

#charger notre joueur
player = Player()

while running :
    
    #appliquer l'arriere plan de notre jeu
    screen.blit(newImage, (0,0))
    
    #vérifier si notre jeu a commencé ou non:
    if game.is_playing:
        #declancher les instruction de la partie
        game.update(screen)
    #si notre jeu n'a pas commencé
    else:
        #ajouter mon ecran de bienvenue 
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
    
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeux en mode "lancé"
                game.is_playing = True
                
                
                


