import pygame
import random
import Sprites_init
import Random_pong

def Level_1():
    pygame.init()
    size = [390,730]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Kawaii catch")
    done = False
    clock = pygame.time.Clock()
    
    black = (0,0,0)
    white = (255, 255, 255)
    
    guy_green = pygame.image.load("pong1_1.png").convert()
    guy_blue = pygame.image.load("pong2_1.png").convert()
    guy_red = pygame.image.load("pong3_1.png").convert()
    guy_yellow = pygame.image.load("pong4_1.png").convert()
    claw_image = pygame.image.load("Claw.png").convert()
    
    pong_green_list = pygame.sprite.Group()
    pong_blue_list = pygame.sprite.Group()
    pong_red_list = pygame.sprite.Group()
    pong_yellow_list = pygame.sprite.Group()
    pong_all_list = pygame.sprite.Group()
    claw_list = pygame.sprite.Group()
    
    claw = Sprites_init.Claw()
    claw.rect.x = size[0]//2 - claw_image.get_width()//2
    claw.rect.y = size[1] - claw_image.get_height()
    claw_list.add(claw)

    timer = 0
    for i in range(1):
        pong_green = Sprites_init.Pong_green()
        pong_blue = Sprites_init.Pong_blue()
        pong_red = Sprites_init.Pong_red()
        pong_yellow = Sprites_init.Pong_yellow()
        pong_green.rect.x = (size[0] - guy_green.get_width()*4)//5
        pong_green.rect.y = - guy_green.get_height()
        pong_blue.rect.x = pong_green.rect.x + guy_green.get_width() + (size[0] - guy_green.get_width()*4)//5
        pong_blue.rect.y = - guy_blue.get_height()
        pong_red.rect.x = pong_blue.rect.x + guy_blue.get_width() + (size[0] - guy_green.get_width()*4)//5
        pong_red.rect.y = - guy_red.get_height()
        pong_yellow.rect.x = pong_red.rect.x + guy_red.get_width() + (size[0] - guy_green.get_width()*4)//5
        pong_yellow.rect.y = - guy_yellow.get_height()
        pong_green_list.add(pong_green)
        pong_blue_list.add(pong_blue)
        pong_red_list.add(pong_red)
        pong_yellow_list.add(pong_yellow)
        pong_all_list.add(pong_green)
        pong_all_list.add(pong_blue)
        pong_all_list.add(pong_red)
        pong_all_list.add(pong_yellow)
    background = pygame.image.load('wallpaper_kawaii.jpg').convert()
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pong_green_list.update()
        timer += 1
        if timer%43 == 0:
            print(timer)
            Random_pong.random_throw(pong_green_list, pong_blue_list, pong_red_list, pong_yellow_list, pong_all_list, guy_green, guy_blue, guy_red, guy_yellow)
        claw_hit_list = pygame.sprite.spritecollide(claw, pong_all_list, False)
        for pong_green in claw_hit_list:
            done = True
        for pong_blue in claw_hit_list:
            done = True
        for pong_red in claw_hit_list:
            done = True
        for pong_yellow in claw_hit_list:
            done = True
        pong_blue_list.update()
        pong_red_list.update()
        pong_yellow_list.update()
        screen.blit(background, [0,0])
        pong_green_list.draw(screen)
        pong_blue_list.draw(screen)
        pong_red_list.draw(screen)
        pong_yellow_list.draw(screen)
        claw_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
Level_1()
