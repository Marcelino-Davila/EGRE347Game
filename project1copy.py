from turtle import pos
import pygame
import sys
import math
import pygame.locals as keys
#import state
#from anim import Animator
#from projectile import projectile
#import actor
#from projectenemy import soldier

pygame.init()
screen = pygame.display.set_mode((800,400))
#pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
#test_font = pygame.font.Font(None, 50)

background_surface = pygame.Surface((800,400))
background_surface.fill('Black')

block_surface = pygame.Surface((100,100))
block_surface.fill('Blue')

block_surface2 = pygame.Surface((100,100))
block_surface2.fill('Yellow')


x_pos = 500
y_pos = 265
y_pos2 = 265
x_pos2 = 100


surface_rect = block_surface.get_rect(midbottom = (200,300))
block_rect = block_surface2.get_rect(midbottom = (80,300))

pos_back = 0
pos_back_down = 0
pos_up = 0

#player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x_pos2 += 5
    if key[pygame.K_LEFT]:
        x_pos2 -= 5

    if block_rect.colliderect(surface_rect):
        print(block_rect.colliderect(surface_rect))

    
    #player_gravity += 1
    #player_rect.y += player_gravity
    #if(player_rect.y > 220):
    #    player_rect.y = 220

    player_gravity += 1
    #block_surface2 += player_gravity
    #if(block_surface2.y > 220):
    #    block_surface2.y = 220

    y_pos2 += player_gravity

    if(y_pos2 > 265):
        y_pos2 = 265

    if(y_pos > 265):
        y_pos = 265



    #screen.blit((0,0))
    #screen.blit((0,300))
    screen.blit(background_surface,(0,0))
    screen.blit(block_surface2,(x_pos2, y_pos2))
    #screen.blit((300, 50))
    #screen.blit(snail_surface,snail_rect)
    #screen.blit(player_surf,player_rect)

    if(x_pos <= 700 and pos_back_down == 1):
        x_pos += 3
        screen.blit(block_surface,(x_pos, y_pos))
        surface_rect.x += 3
        angle = math.atan2(x_pos2 - x_pos,y_pos2 - y_pos)
        print(angle)
    elif(x_pos >= 701):
        pos_up = 1
        pos_back_down = 0
    if(y_pos > 100 and pos_up == 1 and x_pos >= 300):
        y_pos = y_pos - 3
        screen.blit(block_surface,(x_pos, y_pos))
        surface_rect.y -= 3
        angle = math.atan2(x_pos2 - x_pos,y_pos2 - y_pos)
        print(angle)
    elif(y_pos <= 100):
        pos_up = 0
        pos_back = 1
    if(x_pos >= 300 and pos_back == 1 and y_pos <= 100 and pos_back_down != 1):
        x_pos -= 3
        screen.blit(block_surface,(x_pos, y_pos))
        surface_rect.x -= 3
        angle = math.atan2(x_pos2 - x_pos,y_pos2 - y_pos)
        print(angle)
    else:
        pos_back_down = 1
    
    
    #if(x_pos <= 700 and pos_back_down == 1):


    

    pygame.display.update()
    clock.tick(60)