import numpy as np
import matplotlib.pyplot as plt
import pygame
import sys, pygame


m = 1
L = 0
l = 100
g = 5
dt = 1e-2
def rhs(r):
    x,y = r
    return m*g*x


def get_v(L,r):
    x,y = r
    vx = L*y/m/l**2
    vy = -L*x/m/l**2
    return np.array([vx,vy])

def get_accel(v_new,v_old,dt):
    return (v_new-v_old)/dt

def updateL(Lold,r):
    return Lold + dt*rhs(r)


def step(L,r):
    v = get_v(L,r)
    r +=dt*v
    corr = l/np.sqrt(np.sum(r**2)) 
    r *=corr
    L = updateL(L,r)
    return L,r
 
L = 0#150
theta = np.pi/2-0.01
r = l*np.array([np.cos(theta),np.sin(theta)])

animate = True
if animate == True:
    size = width,height = 300, 300
    black = (0,0,0)
    linec = pygame.color.Color('white')
    screen=pygame.display.set_mode(size)

    while 1:
        L,r = step(L,r)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT : sys.exit()
        screen.fill((black))
        
        x,y = r
        print(x,y)
        pygame.draw.line(screen,linec,[150,150],[x+150,-y+150],1)
        pygame.display.flip()



theta = np.pi/3
r = l*np.array([np.cos(theta),np.sin(theta)])
vx,vy=0,0
xx =[]
yy = []
vvx = []
vvy = []
L = 0
LL = []


for t in range(0,10000):
    v = get_v(L,r)
    
    r +=dt*v
    corr = l/np.sqrt(np.sum(r**2)) 
    r *= corr
    L = updateL(L,r)
    xx.append(r[0])
    yy.append(r[1])
    vvx.append(v[0])
    vvy.append(v[1])
    LL.append(L)
plt.plot(xx)
plt.show()
