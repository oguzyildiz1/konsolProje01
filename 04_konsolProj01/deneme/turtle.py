import turtle as t
import time as i
import datetime as d


tur = t.Turtle()

sides = 3
length = 200
angle = 360/ sides

for i in range(sides):
    tur.forward(length)
    tur.right(angle)
