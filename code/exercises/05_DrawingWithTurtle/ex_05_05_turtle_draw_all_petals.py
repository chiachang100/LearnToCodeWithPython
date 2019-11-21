#!/usr/bin/python
# Filename: turtle_05_draw_all_petals.py

import turtle
window = turtle.Screen()
t = turtle.Turtle()

t.left(90)
t.forward(100)

for i in range(1,24):
	t.left(15)
	t.forward(50)
	t.left(157)
	t.forward(50)
window.exitonclick()
