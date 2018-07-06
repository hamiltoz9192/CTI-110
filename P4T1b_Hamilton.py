#CTI-110
#P4T1b - Initials
#Zachary Hamilton
#July 6, 2018
#This program draws my initials ZH

import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

zack = turtle.Turtle()
zack.color("red")
zack.pensize(3)

zack.forward(50)
zack.right(120)
zack.forward(50)
zack.left(120)
zack.forward(50)

zack.penup()
zack.forward(100)
zack.pendown()

zack.left(90)
zack.forward(50)
zack.backward(25)
zack.right(90)
zack.forward(25)
zack.left(90)
zack.forward(25)
zack.backward(50)
