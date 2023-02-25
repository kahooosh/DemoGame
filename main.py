#Importing and initiallizing pygame 
import pygame, sys 
from sys import exit 
pygame.init()

#Creating Display 
screen = pygame.display.set_mode((800,400)) #Creates window ((width,height))
pygame.display.set_caption('Demo Game') #Title of Window
clock = pygame.time.Clock()

#Surfaces and Rectangles
test_font = pygame.font.Font('graphics/Pixeltype.ttf',50) #(type, size)
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('Demo Game', False, (64,64,64)) #(text, AA, color)
    #AA: anti-aliasing; smoothing edges of the text (put true for non-pixel and false for other)
score_rect = score_surf.get_rect(center = (400,50))


en1_surf = pygame.image.load('graphics/snail1.png').convert_alpha() #enemy 1 
en1_rect = en1_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player_walk_1.png') #player
player_rect = player_surf.get_rect(midbottom = (80,300))
    #pygame.Rect(); player rectangle 
    #(left,top,width,height)
    #(topleft = (x,y))
player_gravity = 0 

"""
# Surfaces Example 
test_surface = pygame.Surface((100,200)) #((w,h))
test_surface.fill('Red') #Adds color 
"""

#Draw all elements and update everything
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #pos of mouse when moving 
            if player_rect.collidepoint(event.pos): 
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    #Putting Surfaces and Rectangles on Display 
    screen.blit(sky_surf, (0,0)) # (0,0) is top left 
        #Blit = Block image transfer, one surface on another; arguement = (surface, pos)
    screen.blit(ground_surf, (0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect) #(display, color, rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10,50) #border width
    screen.blit(score_surf,score_rect) 

    #Enemy_1 Movememnt 
    en1_rect.x -= 4  
    if en1_rect.right <= 0: en1_rect.left = 800 
    screen.blit(en1_surf,en1_rect) 
    """ Another way to move en1: 
    en1_x_pos -= 4 #moves to left every loop
    if en1_x_pos < -100: en1_x_pos = 800 #brings back en1 to the right side 
    """

    #Player Movement 
    player_gravity += 1 
    player_rect.y += player_gravity
    if player_rect >= 300:
        player_rect.bottem = 300
    screen.blit(player_surf,player_rect)


 
    pygame.display.update()
    clock.tick(60) #sets maximum frame rate (fps )
       