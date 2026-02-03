from pygame import *
from random import *
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

width = 800
height = 600
s_size = (width, height)
screen = display.set_mode(s_size)
s_Color = black
clock = time.Clock()

player = [width/2 , height/2]

x = width/2 
y = height/2
vx = 5
vy = 5
r = randint(5, 20)

P_num = 2
range_x = (r,width-r)
range_y = (r, height-r)
range_vx = (-5 , 5)
range_vy = (-5 , 5)
