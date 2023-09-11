from turtle import *


def drawSpiral(lineLen):
    setheading(0)
    # Initialize the length for the spiral
    length = lineLen

    # Draw the spiral
    while length > 0:
        forward(length)
        right(90)
        length -= 5

    return


# To test the function
drawSpiral(4)  # Draws a square spiral with the longest line being 100 units
done()