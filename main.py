#BASIC SET UP FOR GAME 

#Importing and initiallizing pygame 
import pygame, sys 
from sys import exit 
pygame.init()

#Creating Display 
screen = pygame.display.set_mode((800,400)) #Creates window ((width,height))
pygame.display.set_caption('Demo Game') #Title of Window
clock = pygame.time.Clock()

#Surfaces and Fonts 
test_font = pygame.font.Font('graphics/Pixeltype.ttf',50) #(type, size)
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('Demo Game', False, 'Green') #(text, AA, color)
#AA: anti-aliasing; smoothing edges of the text (put true for non-pixel and false for other)

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

    pygame.display.update()
    clock.tick(60) #sets maximum frame rate (fps )
    