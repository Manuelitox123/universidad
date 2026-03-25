# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 13:19:48 2025

@author: dagob
"""

import turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range (360) : 
    t.color(colors[i % len(colors)])
    t.forward(i * 2 / len(colors) + i)
    t.left(120)
    t.left(1)
    
turtle.done()