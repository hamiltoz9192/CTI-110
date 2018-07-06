#CTI-110
#P4T1a - Shapes
#Zachary Hamilton
#July 6, 2018
#This program draws a square and a triangle

import turtle
wn = turtle.Screen()
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
for i in range(3):
    turtle.forward(50)
    turtle.left(120)
