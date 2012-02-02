# coding=utf-8

"""

* File Name : main.pyw

* Created By : Natan Žabkar, natan.zabkar@gmail.com 

* Creation Date : 02-02-2012

* Last Modified : 2.2.2012 2:31:09

"""


import pygame


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


width = 600
height = 600

w = width//50
h = height//50

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


running = True

screen.fill(white)
for i in range(w, width, w):
    pygame.draw.line(screen, black, (i,0), (i,height))
for i in range(h, height, h):
    pygame.draw.line(screen, black, (0,i), (height,i))

pygame.display.flip()

while running:



    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

