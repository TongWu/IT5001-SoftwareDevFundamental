from turtle import *
import time

def koch_snowflake(iterations, length=200):
    if iterations == 0:
        forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(iterations-1, length/3)
            left(angle)

def draw_snowflake(iterations):
    speed(0)
    for _ in range(3):
        koch_snowflake(iterations)
        right(120)
    done()

iterations = int(time.time()) % 4 + 1
draw_snowflake(iterations)