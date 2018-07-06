#CTI-110
#P4LAB - Nested Loops
#Zachary Hamilton
#July 6, 2018
#This program draws a nested loop.

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

zack = turtle.Turtle()
zack.color("red")
zack.pensize(3)
for x in range(6):
    for i in range(6):
        zack.forward(30)
        zack.left(60)
    zack.left(60)
