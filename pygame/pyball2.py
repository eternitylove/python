#!/usr/bin/env python


import os
import sys

import pygame
from pygame.locals import *

speed=[0,0]
def load_image(pic_name):
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(current_dir,'image',pic_name)
    return pygame.image.load(path).convert()

def control_ball(event):
    global speed
    speed_offset = 1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed[0]-=speed_offset
        if event.key == pygame.K_RIGHT:
            speed[0]+=speed_offset
        if event.key == pygame.K_UP:
            speed[1]-=speed_offset
        if event.key == pygame.K_DOWN:
            speed[1]+=speed_offset
    if event.type in (pygame.KEYUP,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_DOWN) :
        speed=[0,0]

    return speed

def play_ball():
    pygame.init()
    window_size = Rect(0,0,700,500)
    screen = pygame.display.set_mode(window_size.size)
    pygame.display.set_caption("moving ball")
    ball_image = load_image('ball.png')

    back_image = load_image('back_image.jpg')
    ball_rect = ball_image.get_rect()   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

            control_ball(event)

            ball_rect = ball_rect.move(speed)
            screen.blit(back_image,(0,0))
            screen.blit(ball_image,ball_rect)
            pygame.display.update()

if __name__ == '__main__':

    play_ball()
