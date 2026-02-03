from pygame import *
from variables import *


class particle:
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r 
        self.vx = vx
        self.vy = vy

    def move(self):

        self.x+=self.vx
        self.y+=self.vy
        if self.x + self.r >= screen.get_width() or self.x-self.r <= 0:
            self.vx = -self.vx
    
        if (self.y+self.r)>=screen.get_height() or self.y-self.r <= 0:
            self.vy = -self.vy

        
        draw.circle(screen, white, (self.x,self.y), self.r, 0)

def  screen_F():
    screen.fill(s_Color)



def key_P(event):
    global running, x, y

    for i in event:
        if i.type == QUIT:
            running = False

        elif i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                exit()
            elif i.key == K_a:
                player[0] +=5

