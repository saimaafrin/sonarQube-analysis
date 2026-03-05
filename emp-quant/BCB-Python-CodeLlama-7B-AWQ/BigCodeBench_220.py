from random import choice
import turtle
import time
def task_func(colors):
    """
    Draws five squares of random colors using Turtle Graphics. Each square is drawn sequentially with a 1-second pause between squares. The function requires a list of colors as input and sets up a Turtle Graphics window, creates a Turtle object, and uses it to draw the squares with colors from the provided list. The window remains open after drawing.
    """
    # Set up Turtle Graphics window
    turtle.setup(width=500, height=500)
    turtle.title("Turtle Graphics")
    turtle.bgcolor("white")
    turtle.tracer(0)

    # Create Turtle object
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-250, -250)
    t.pendown()

    # Draw squares with colors from the provided list
    for i in range(5):
        t.color(choice(colors))
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        time.sleep(1)

    # Keep window open
    turtle.done()
colors = ["red", "green", "blue", "yellow", "orange"]