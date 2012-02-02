# coding=utf-8

"""

* File Name : main.pyw

* Created By : Natan Žabkar, natan.zabkar@gmail.com 

* Creation Date : 02-02-2012

* Last Modified : 2.2.2012 2:21:38

"""


import pygame



width = 800
height = 600


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


running = True

while running:

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

