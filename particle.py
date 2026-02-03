from pygame import *
from random import *
from functions import *
from variables import * 

c=[]
for i in range(P_num):
    i = particle(randint(*range_x),
                 randint(*range_y),
                 randint(5, 20),
                 randint(*range_vx),
                 randint(*range_vy)
                 )
    c.append(i)

running = True

init()

while running:
    key_P(event.get())
    screen_F()
    for i in c:
        i.move()
    display.flip()
    clock.tick(60)

quit()
