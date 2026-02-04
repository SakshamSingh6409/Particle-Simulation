from pygame import *
from random import *
from functions import *
from variables import * 


init()
spawn_P()

while running:
    screen_F()
    for i in c:
        i.move()
    key_P(event.get())
    display.flip()
    clock.tick(60)
    
