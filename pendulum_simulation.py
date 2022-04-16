import numpy as np
import matplotlib.pyplot as plt
import pygame
import sys, pygame


m = 1
L = 0
r = 100
g = 5
dt = 1e-2
def rhs(r):
    x,y = r
    return m*g*x


def get_v(L,x,y):
    vx = L*y/m/r**2
    vy = -L*x/m/r**2

    return vx,vy

def updateL(Lold,r,vx,vy):
    
    return Lold + dt*rhs(r)


def step(L,x,y):
    vx,vy = get_v(L,x,y)
    x += vx*dt
    y += vy*dt
    corr = r/(x**2+y**2)**0.5    
    x = corr*x
    y = corr*y

    L = updateL(L,[x,y],vx,vy)
    return L,x,y
 
size = width,height = 300, 300
black = (0,0,0)
linec = pygame.color.Color('white')
screen=pygame.display.set_mode(size)
L = 0#150
theta = np.pi/2-0.01
x,y = r*np.cos(theta),r*np.sin(theta)

while 1:
    L,x,y = step(L,x,y)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()
    screen.fill((black))
    pygame.draw.line(screen,linec,[150,150],[int(x)+150,-int(y)+150],2)
    pygame.display.flip()



theta = np.pi/2-0.1
x,y = r*np.cos(theta),r*np.sin(theta)
vx,vy=0,0
xx =[]
yy = []
vvx = []
vvy = []
L = 0
LL = []


for t in range(0,10000):
    vx,vy = get_v(L,x,y)
    x += vx*dt
    y += vy*dt
    corr = r/(x**2+y**2)**0.5    
    x = corr*x
    y = corr*y

    L = updateL(L,[x,y],vx,vy)
    xx.append(x)
    yy.append(y)
    vvx.append(vx)
    vvy.append(vy)
    LL.append(L)
