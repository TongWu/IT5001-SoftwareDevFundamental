from turtle import *

def drawRegPoly(l,n):
    angle = 360 / n
    for _ in range(n):
        forward(l)
        left(angle)
    return 0 #write your code here

drawRegPoly(100,8)