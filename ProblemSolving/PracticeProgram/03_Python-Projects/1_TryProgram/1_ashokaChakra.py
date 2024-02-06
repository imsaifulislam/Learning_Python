from turtle import *
color("red")
width(3)
x = 200
speed(10)

for i in range(36):
    forward(x)
    setposition(0,0)
    left(10)

width(4)
forward(x)
left(90)
circle(200)
done()