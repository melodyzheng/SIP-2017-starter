
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
color = input("What color?")

pencolor(color)

setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)
x= 0
begin_fill()
s = input("How many sides?")
for x in range (s):
    forward(50)
    right(360/int(s))
    x = x+1

fillcolor(color)
end_fill()


### Write your code below:

