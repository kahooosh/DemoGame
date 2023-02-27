#Importing and initiallizing pygame 
import pygame, sys 
from sys import exit 
from random import randint
pygame.init()

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list): 
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5 

            screen.blit(en1_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else:
        return []


#CREATING DISPLAY 
screen = pygame.display.set_mode((800,400)) #Creates window ((width,height))
pygame.display.set_caption('Demo Game') #Title of Window
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0


#SURFACES AND RECTANGLES 
"""
# Surfaces Example 
test_surface = pygame.Surface((100,200)) #((w,h))
test_surface.fill('Red') #Adds color 
"""

#Sky and Ground 
test_font = pygame.font.Font('graphics/Pixeltype.ttf',50) #(type, size)
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

#Intro/Game Over Screen
game_title = test_font.render('Pixel Runner',False,(37,56,74))
game_title = pygame.transform.rotozoom(game_title,0,2)
game_title_rect = game_title.get_rect(center = (400,60))

game_over = test_font.render('GAME OVER',False,(37,56,74))
game_over = pygame.transform.rotozoom(game_over,0,2)
game_over_rect = game_over.get_rect(center = (400,60))

press_space = test_font.render('Press space bar to restart',False,'White')
press_space = pygame.transform.rotozoom(press_space,0,0.80)
press_space_rect = press_space.get_rect(center = (400,330))

#Obstacles 
en1_surf = pygame.image.load('graphics/snail1.png').convert_alpha() #enemy 1 

en2_surf = pygame.image.load('graphics/Fly1.png').convert_alpha() #enemy 2 

obstacle_rect_list = []

#Player 
player_surf = pygame.image.load('graphics/player_walk_1.png') #player
player_rect = player_surf.get_rect(midbottom = (80,300))
    #pygame.Rect(); player rectangle 
    #(left,top,width,height)
    #(topleft = (x,y))
player_gravity = 0 
player_stand = pygame.image.load('graphics/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,1.5) #(surf,rotation,scale); scales and rotate 
player_stand_rect = player_stand.get_rect(center = (400,200))

#Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500) #(event we want to trigger, how often to trigger in millisec.)


#DRAW ALL ELEMENTS AND UPDATE
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: #pos of mouse when moving 
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(en1_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(en2_surf.get_rect(bottomright = (randint(900,1100),210)))

    if game_active:
        #Putting Surfaces and Rectangles on Display 
        screen.blit(sky_surf, (0,0)) # (0,0) is top left 
            #Blit = Block image transfer, one surface on another; arguement = (surface, pos)
        screen.blit(ground_surf, (0,300))
        """ Demo Game TItle 
        pygame.draw.rect(screen,'#c0e8ec',score_rect) #(display, color, rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,10,50) #border width
        screen.blit(score_surf,score_rect) 
        """
        score = display_score()

        """
        #Enemy_1 Movememnt 
        en1_rect.x -= 4  
        if en1_rect.right <= 0: en1_rect.left = 800 
        screen.blit(en1_surf,en1_rect) 

        Another way to move en1: 
        en1_x_pos -= 4 #moves to left every loop
        if en1_x_pos < -100: en1_x_pos = 800 #brings back en1 to the right side 
        """

        #Player Movement 
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #Obstacle  Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #Collision 
    
    #Title and Game Over Screen  
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(press_space,press_space_rect)

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,110))

        if score == 0:
            screen.blit(game_title,game_title_rect)  
        else:
            screen.blit(game_over,game_over_rect)
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60) #sets maximum frame rate (fps )
       