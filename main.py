#Importing and initiallizing pygame 
import pygame, sys 
from sys import exit 
pygame.init()

#Creating Display 
screen = pygame.display.set_mode((800,400)) #Creates window ((width,height))
pygame.display.set_caption('Demo Game') #Title of Window
clock = pygame.time.Clock()

#Surfaces 
test_font = pygame.font.Font('graphics/Pixeltype.ttf',50) #(type, size)
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Demo Game', False, 'Black ') #(text, AA, color)
    #AA: anti-aliasing; smoothing edges of the text (put true for non-pixel and false for other)

en1_surface = pygame.image.load('graphics/snail1.png').convert_aplpha() #enemy 1 
en1_x_pos = 600 #pos of en1 
player_surf = pygame.image.load('graphics/player_walk_one.png') #player
player_rect = player_surf.get_rect(topleft = (x,y))
    #pygame.Rect(); player rectangle 
    #(left,top,width,height)
    #(topleft = (x,y))

"""
#Surfaces Example 
test_surface = pygame.Surface((100,200)) #((w,h))
test_surface.fill('Red') #Adds color 
"""

#Draw all elements and update everything
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    #Blit = Block image transfer, one surface on another; arguement = (surface, pos)
    screen.blit(sky_surface, (0,0)) # (0,0) is top left 
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))
    en1_x_pos -= 4 #moves to left every loop
    if en1_x_pos < -100: en1_x_pos = 800 #brings back en1 to the right side 
    screen.blit(en1_surface, (en1_x_pos,250)) 
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60) #sets maximum frame rate (fps )
       