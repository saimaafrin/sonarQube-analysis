
from random import choice
import turtle
import time

def task_func(colors):
    # Set up Turtle Graphics window
    window = turtle.Screen()
    window.setup(width=600, height=600)
    window.title("Squares with Random Colors")

    # Create Turtle object
    turtle = turtle.Turtle()
    turtle.speed(0)

    # Draw squares with random colors
    for i in range(5):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.color(choice(colors))
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        time.sleep(1)

    # Keep window open
    window.mainloop()