import pygame
import random
import Sprites_init

pygame.init()
size = [390, 730]

class Get_rect():
    get_x = 0
    get_y = 0

def random_throw (green_list, blue_list, red_list, yellow_list, brown_list, purple_list, all_list, green, blue, red, yellow, brown, purple):
        choice = random.randint(0, 5)
        if choice == 0:
            pong_green = Sprites_init.Pong_green()
            green_list.add(pong_green)
            all_list.add(pong_green)
            pong_green.rect.x = (size[0] - green.get_width()*8)//9
            pong_green.rect.y = - green.get_height()
            Rect = Get_rect()
            Rect.get_x = pong_green.rect.x
            Rect.get_y = pong_green.rect.y
            print(Rect.get_x)
            print(Rect.get_y)
        elif choice == 1:
            pong_blue = Sprites_init.Pong_blue()
            pong_blue.rect.x = (size[0] - blue.get_width()*8)//9
            pong_blue.rect.y = - blue.get_height()
            blue_list.add(pong_blue)
            all_list.add(pong_blue)
        elif choice == 2: 
            pong_red = Sprites_init.Pong_red()
            pong_red.rect.x = (size[0] - red.get_width()*8)//9
            pong_red.rect.y = - red.get_height()
            red_list.add(pong_red)
            all_list.add(pong_red)
        elif choice == 3:
            pong_yellow = Sprites_init.Pong_yellow()
            pong_yellow.rect.x = (size[0] - yellow.get_width()*8)//9
            pong_yellow.rect.y = - yellow.get_height()
            yellow_list.add(pong_yellow)
            all_list.add(pong_yellow)
        elif choice == 4:
            pong_brown = Sprites_init.Pong_brown()
            pong_brown.rect.x = (size[0] - brown.get_width()*8)//9
            pong_brown.rect.y = - brown.get_height()
            brown_list.add(pong_brown)
            all_list.add(pong_brown)
        elif choice == 5:
            pong_purple = Sprites_init.Pong_purple()
            pong_purple.rect.x = (size[0] - purple.get_width()*8)//9
            pong_purple.rect.y = - purple.get_height()
            purple_list.add(pong_purple)
            all_list.add(pong_purple)
        latest_choice = choice
        choice = 0
        for i in range (7):
                choice = random.randint(0, 5)
                if latest_choice == 0:
                    nesses_rect = pong_green.rect.x
                elif latest_choice == 1:
                    nesses_rect = pong_blue.rect.x
                elif latest_choice == 2:
                    nesses_rect = pong_red.rect.x
                elif latest_choice == 3:
                    nesses_rect = pong_yellow.rect.x
                elif latest_choice == 4:
                    nesses_rect = pong_brown.rect.x
                elif latest_choice == 5:
                    nesses_rect = pong_purple.rect.x
                
                if choice == 0:
                    pong_green = Sprites_init.Pong_green()
                    green_list.add(pong_green)
                    all_list.add(pong_green)
                    pong_green.rect.x = nesses_rect + green.get_width() + (size[0] - green.get_width()*8)//9
                    pong_green.rect.y = - green.get_height()    
                elif choice == 1:
                    pong_blue = Sprites_init.Pong_blue()
                    pong_blue.rect.x = nesses_rect + blue.get_width() + (size[0] - blue.get_width()*8)//9
                    pong_blue.rect.y = - blue.get_height()
                    blue_list.add(pong_blue)
                    all_list.add(pong_blue)
                elif choice == 2:
                    pong_red = Sprites_init.Pong_red()
                    pong_red.rect.x = nesses_rect + red.get_width() + (size[0] - red.get_width()*8)//9
                    pong_red.rect.y = - red.get_height()
                    red_list.add(pong_red)
                    all_list.add(pong_red)
                elif choice == 3:
                    pong_yellow = Sprites_init.Pong_yellow()
                    pong_yellow.rect.x = nesses_rect + yellow.get_width() + (size[0] - yellow.get_width()*8)//9
                    pong_yellow.rect.y = - yellow.get_height()
                    yellow_list.add(pong_yellow)
                    all_list.add(pong_yellow)
                elif choice == 4:
                    pong_brown = Sprites_init.Pong_brown()
                    pong_brown.rect.x = nesses_rect + brown.get_width() + (size[0] - brown.get_width()*8)//9
                    pong_brown.rect.y = - brown.get_height()
                    brown_list.add(pong_brown)
                    all_list.add(pong_brown)
                elif choice == 5:
                    pong_purple = Sprites_init.Pong_purple()
                    pong_purple.rect.x = nesses_rect + purple.get_width() + (size[0] - purple.get_width()*8)//9
                    pong_purple.rect.y = - purple.get_height()
                    purple_list.add(pong_purple)
                    all_list.add(pong_purple)
                latest_choice = choice
                choice = 0
                nesses_rect = 0

