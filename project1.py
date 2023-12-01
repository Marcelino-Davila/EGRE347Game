from turtle import pos
import pygame
import sys
import pygame.locals as keys

pygame.init()
screen = pygame.display.set_mode((800,400))
#pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
#test_font = pygame.font.Font(None, 50)

background_surface = pygame.Surface((800,400))
background_surface.fill('Black')

block_surface = pygame.Surface((100,100))
block_surface.fill('Blue')

x_pos = 500
y_pos = 265
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
    
    #player_gravity += 1
    #player_rect.y += player_gravity
    #if(player_rect.y > 220):
    #    player_rect.y = 220

    #y_pos += player_gravity
    if(y_pos > 265):
        y_pos = 265



    #screen.blit((0,0))
    #screen.blit((0,300))
    screen.blit(background_surface,(0,0))
    screen.blit(block_surface,(100, 300))
    #screen.blit((300, 50))
    #screen.blit(snail_surface,snail_rect)
    #screen.blit(player_surf,player_rect)

    if(x_pos <= 700 and pos_back_down == 1):
        x_pos += 3
        screen.blit(block_surface,(x_pos, y_pos))
    elif(x_pos >= 701):
        pos_up = 1
        pos_back_down = 0
    if(y_pos > 100 and pos_up == 1 and x_pos >= 300):
        y_pos = y_pos - 3
        screen.blit(block_surface,(x_pos, y_pos))
    elif(y_pos <= 100):
        pos_up = 0
        pos_back = 1
    if(x_pos >= 300 and pos_back == 1 and y_pos <= 100 and pos_back_down != 1):
        x_pos -= 3
        screen.blit(block_surface,(x_pos, y_pos))
    else:
        pos_back_down = 1
    if(x_pos >= 700 and pos_back_down == 0 and y_pos > 100):
        y_pos = y_pos + 3
        screen.blit(block_surface,(x_pos, y_pos))
    else:
        pos_back_down = 1
    

    pygame.display.update()
    clock.tick(60)