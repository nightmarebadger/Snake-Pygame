# coding=utf-8

"""

* File Name : main.pyw

* Created By : Natan Žabkar, natan.zabkar@gmail.com 

* Creation Date : 02-02-2012

* Last Modified : 2.2.2012 3:09:37

"""


import pygame


def drawSquare(screen, position, color):
    """
        Draw on the screen on position x, y (x and y are not coordinates, they're the grid position!)
        Upperleft square is 0,0
    """
    screen.fill(color, (position[0] * w + 1, position[1] * h + 1, w - 1, h - 1))


class Snake:
    def __init__(self, screen, bgcolor, x, y, color, grow_to = 2):
        self.screen = screen
        self.bgcolor = bgcolor
        self.x = x
        self.y = y
        self.color = color
        self.grow_to = grow_to
        
        self.vx = 0
        self.vy = 0
        self.body = []
        self.crashed = False
        self.length = 1

        self.speed = 1


    def keyHandler(self, event):

        if(event.key == pygame.K_UP and self.vy <= 0):
            self.vx = 0
            self.vy = -self.speed
        elif(event.key == pygame.K_DOWN and self.vy >= 0):
            self.vx = 0
            self.vy = self.speed
        elif(event.key == pygame.K_LEFT and self.vx <= 0):
            self.vx = -self.speed
            self.vy = 0
        elif(event.key == pygame.K_RIGHT and self.vx >= 0):
            self.vx = self.speed
            self.vy = 0



    def draw(self):
        # Initial draw, other drawing will be done in move function
        drawSquare(self.screen, (self.x,self.y), self.color)

    def move(self):

        self.body.insert(0, (self.x, self.y))

        self.x += self.vx
        self.y += self.vy

        if((self.x, self.y) in self.body):
            self.crashed = True

        # Draw the head that moved
        drawSquare(self.screen, (self.x,self.y), self.color)

        if(self.grow_to > self.length):
            self.length += 1

        # If too long, pop the last element of body and "delete" that square
        if(len(self.body) > self.length):
            drawSquare(self.screen, self.body.pop(), self.bgcolor)


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

#drawSquare(screen, (2,3), blue)

snake = Snake(screen, white, 24, 24, black)
snake.draw()

pygame.display.flip()

while running:

    snake.move()

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.KEYDOWN):
            snake.keyHandler(event)

    pygame.display.flip()
    clock.tick(5)
