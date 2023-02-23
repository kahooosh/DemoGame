#BASIC SET UP FOR GAME 

#Importing and initiallizing pygame 
import pygame, sys 
from sys import exit 
pygame.init()

#Creating Display 
screen = pygame.display.set_mode((800,400)) # Creates window((width,height))
pygame.display.set_caption('Demo Game') #Title of Window
pygame.time.Clock()

#Draw all elements and update everything
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
    pygame.display.update()
    clock.tick(60) 

