import turtle
from turtle import *

def drawFlower(l, p, n):
    # embed polygon function
    def drawRegPoly(l, p):
        angle = 360 / p
        for _ in range(p):
            forward(l)
            left(angle)
        return 0

    petal_angle = 360 / n
    for _ in range(n):
        drawRegPoly(l, p)
        left(petal_angle)

    return 0  # write your code here

drawFlower(100,8,10)
turtle.done()