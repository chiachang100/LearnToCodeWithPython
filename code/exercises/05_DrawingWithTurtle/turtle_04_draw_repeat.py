#!/usr/bin/python
# Filename: turtle_04_draw_repeat.py

import turtle

window = turtle.Screen()
t = turtle.Turtle()

for x in range(0, 4):
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(10)
    t.right(90)
    
window.exitonclick()
