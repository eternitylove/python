#!/usr/bin/env python

# coding:utf-8

import sys
import pygame

from pygame.locals import *

def play_ball():
    pygame.init()

    window_size = (width,height)=(700,500)

    speed = [1,1]

    color_black=(0,0,139)

    screen = pygame.display.set_mode(window_size)
    
    ball_image=pygame.image.load("ball.png")

    ball_rect=ball_image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            ball_rect = ball_rect.move(speed)
            if(ball_rect.left<0) or (ball_rect.right>width):
                speed[0]=-speed[0]

            if(ball_rect.top<0) or (ball_rect.bottom>height):
                speed[1]=-speed[1]
            screen.fill(color_black)

            screen.blit(ball_image,ball_rect)

            pygame.display.update()

if __name__=='__main__':

    play_ball()
