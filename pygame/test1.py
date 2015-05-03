#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)

def create_scales(height):
	reds=pygame.surface.Surface((640,height))
	greens=pygame.surface.Surface((640,height))
	blues=pygame.surface.Surface((640,height))

	for x in xrange(640):
		c=int((x/640.)*255)
		red=(c,0,0)
		green=(0,c,0)
		blue=(0,0,c)
		line_rect=Rect(x,0,1,height)
		pygame.draw.rect(reds,red,line_rect)
		pygame.draw.rect(greens,green,line_rect)
		pygame.draw.rect(blues,blue,line_rect)
	return reds,greens,blues
red_scale,green_scale,blue_scale = create_scales(80)
color=[127,127,127]
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	screen.fill((0,0,0))
	screen.blit(red_scale,(0,00))
	screen.blit(green_scale,(0,80))
	screen.blit(blue_scale,(0,160))
	
	x,y=pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
	 	for component in range(3):
			if y>component*80 and y<(component+1)*80:
				color[component]=int((x/639.)*255)
		pygame.display.set_caption("color test")
	for component in range(3):
		pos = (int((color[component]/255)*639),component*80+40)
		pygame.draw.circle(screen,(255,255,255),pos,20)
	
	pygame.draw.rect(screen,tuple(color),(0,240,640,240))
	pygame.display.update()
