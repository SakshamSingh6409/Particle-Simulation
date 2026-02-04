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
            End()

        elif i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                End()
            elif i.key == K_a:
                player[0] +=5



def spawn_P():
    for i in range(P_num):
        x_t = randint(*range_x)
        y_t = randint(*range_y)
        r_t = randint(*range_r)
        vx_t = randint(*range_vx)
        vy_t = randint(*range_vy)
        i = particle(x_t,
                     y_t,
                     r_t,
                     vx_t,
                     vy_t                 
                    )
        c.append(i)
        x.append(x_t)
        y.append(y_t)
        r.append(r_t)
        vx.append(vx_t)
        vy.append(vy_t)

def End():
    print(f"c: {c}")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"r: {r}")
    print(f"vx: {vx}")
    print(f"vy: {vy}")
    quit()
