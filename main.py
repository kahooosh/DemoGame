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
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('Demo Game', False, 'Black ') #(text, AA, color)
    #AA: anti-aliasing; smoothing edges of the text (put true for non-pixel and false for other)

en1_surf = pygame.image.load('graphics/snail1.png').convert_alpha() #enemy 1 
en1_rect = en1_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player_walk_1.png') #player
player_rect = player_surf.get_rect(midbottom = (80,300))
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
    screen.blit(sky_surf, (0,0)) # (0,0) is top left 
    screen.blit(ground_surf, (0,300))
    screen.blit(text_surf, (300,50))

    """
    Another way to move en1 
    en1_x_pos -= 4 #moves to left every loop
    if en1_x_pos < -100: en1_x_pos = 800 #brings back en1 to the right side 
    """

    en1_rect.x -= 4  
    if en1_rect.right <= 0: en1_rect.left = 800 
    screen.blit(en1_surf,en1_rect) 
    screen.blit(player_surf,player_rect)

    #if player_rect.colliderect(en1_rect):
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos): #((x,y)):
        print("collision")
    
    pygame.display.update()
    clock.tick(60) #sets maximum frame rate (fps )
       