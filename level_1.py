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
    guy_brown = pygame.image.load("pong5_1.png").convert()
    guy_purple = pygame.image.load("pong6_1.png").convert()
    claw_image = pygame.image.load("Claw.png").convert()

    pong_green_list = pygame.sprite.Group()
    pong_blue_list = pygame.sprite.Group()
    pong_red_list = pygame.sprite.Group()
    pong_yellow_list = pygame.sprite.Group()
    pong_brown_list = pygame.sprite.Group()
    pong_purple_list = pygame.sprite.Group()
    pong_all_list = pygame.sprite.Group()
    claw_list = pygame.sprite.Group()

    weapon_list = pygame.sprite.Group()
    weapon_ch = random.randint(0,5)
    if weapon_ch == 0:
        pong_weap = Sprites_init.Pong_weapon_1()
        weapon_list.add(pong_weap)
    if weapon_ch == 1:
        pong_weap = Sprites_init.Pong_weapon_2()
        weapon_list.add(pong_weap)
    if weapon_ch == 2:
        pong_weap = Sprites_init.Pong_weapon_3()
        weapon_list.add(pong_weap)
    if weapon_ch == 3:
        pong_weap = Sprites_init.Pong_weapon_4()
        weapon_list.add(pong_weap)
    if weapon_ch == 4:
        pong_weap = Sprites_init.Pong_weapon_5()
        weapon_list.add(pong_weap)
    if weapon_ch == 5:
        pong_weap = Sprites_init.Pong_weapon_6()
        weapon_list.add(pong_weap)
    
    pause = (size[0] - guy_red.get_width()*8)//9
    movement = [pause, pause*2 + claw_image.get_width(), pause*3 + claw_image.get_width()*2,
                pause*4 + claw_image.get_width()*3, pause*5 + claw_image.get_width()*4, pause*6 + claw_image.get_width()*5,
                pause*7 + claw_image.get_width()*6, pause*8 + claw_image.get_width()*7]
    claw = Sprites_init.Claw()
    claw_list.add(claw)
    shot = 0
    y = 3
    timer = 0
    weap_mov = 0
    ness_x = 0
    ness_y = 0
    Random_pong.random_throw(pong_green_list, pong_blue_list, pong_red_list, pong_yellow_list, pong_brown_list, pong_purple_list,
                             pong_all_list, guy_green, guy_blue, guy_red, guy_yellow, guy_brown, guy_purple)
    background = pygame.image.load('wallpaper_kawaii.jpg').convert()
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if y > 0:
                        y -= 1
                    else:
                        y = 7
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if y < 7:
                        y += 1
                    else:
                        y = 0
                if event.key == pygame.K_SPACE and shot != 1:
                    shot = 1
                    weapon_pos = movement[y]
                if event.key == pygame.K_SPACE and shot == 1:
                    pass
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    y -= 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    y += 0
        timer += 1
        if timer%43 == 0:
            Random_pong.random_throw(pong_green_list, pong_blue_list, pong_red_list, pong_yellow_list, pong_brown_list, pong_purple_list,
                                     pong_all_list, guy_green, guy_blue, guy_red, guy_yellow, guy_brown, guy_purple)
        claw_hit_list = pygame.sprite.spritecollide(claw, pong_all_list, False)
        for pong in claw_hit_list:
            done = True
        
        green_hit_list = pygame.sprite.spritecollide(pong_weap, pong_green_list, False)
        blue_hit_list = pygame.sprite.spritecollide(pong_weap, pong_blue_list, False)
        red_hit_list = pygame.sprite.spritecollide(pong_weap, pong_red_list, False)
        yellow_hit_list = pygame.sprite.spritecollide(pong_weap, pong_yellow_list, False)
        brown_hit_list = pygame.sprite.spritecollide(pong_weap, pong_brown_list, False)
        purple_hit_list = pygame.sprite.spritecollide(pong_weap, pong_purple_list, False)
        for pong_green in green_hit_list:
            shot = 2
            pos = pong_green.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_green.rect.y + 43
        for pong_blue in blue_hit_list:
            shot = 2
            pos = pong_blue.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_blue.rect.y + 43
        for pong_red in red_hit_list:
            shot = 2
            pos = pong_red.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_red.rect.y + 43
        for pong_yellow in yellow_hit_list:
            shot = 2
            pos = pong_yellow.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_yellow.rect.y + 43
        for pong_brown in brown_hit_list:
            shot = 2
            pos = pong_brown.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_brown.rect.y + 43
        for pong_purple in purple_hit_list:
            shot = 2
            pos = pong_purple.rect.y
            ness_x = pong_weap.rect.x
            ness_y = pong_purple.rect.y + 43
        claw.rect.x = movement[y]
        claw.rect.y = size[1] - claw_image.get_height()
        
        if shot == 0:
            pong_weap.rect.x = movement[y]
            pong_weap.rect.y = size[1] - claw_image.get_height() - 10
        elif shot == 1:
            weap_mov = 40
            pong_weap.rect.x = weapon_pos
            pong_weap.rect.y -= weap_mov
        elif shot == 2:
            weap_mov = 0
            pong_blue = Sprites_init.Pong_blue()
            pong_blue.rect.x = ness_x
            pong_blue.rect.y = ness_y
            pong_blue_list.add(pong_blue)
            pong_all_list.add(pong_blue)
            weapon_list.remove(pong_weap)
            
            pong_weap = Sprites_init.Pong_weapon_2()
            weapon_list.add(pong_weap)
            pong_weap.rect.x = movement[y]
            pong_weap.rect.y = size[1] - claw_image.get_height() - 10
            shot = 0
        pong_green_list.update()
        pong_blue_list.update()
        pong_red_list.update()
        pong_yellow_list.update()
        pong_brown_list.update()
        pong_purple_list.update()
        screen.blit(background, [0,0])
        pong_green_list.draw(screen)
        pong_blue_list.draw(screen)
        pong_red_list.draw(screen)
        pong_yellow_list.draw(screen)
        pong_brown_list.draw(screen)
        pong_purple_list.draw(screen)
        weapon_list.draw(screen)
        claw_list.draw(screen)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()
Level_1()
