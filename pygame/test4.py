#!/usr/bin/env python


fish='sea.jpg'
back = 'fish.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(back).convert()
sprite=pygame.image.load(fish)
x=0.
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	
	screen.blit(background,(0,0))
	screen.blit(sprite,(x,100))
	x+=5
	if x>640:
		x=0
	pygame.display.update()
