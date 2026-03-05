from random import choice
import turtle
import time
def task_func(colors):
    """
    Draws five squares of random colors using Turtle Graphics.
    Each square is drawn sequentially with a 1-second pause between squares.
    The function requires a list of colors as input and sets up a Turtle Graphics window,
    creates a Turtle object, and uses it to draw the squares with colors from the provided list.
    The window remains open after drawing.
    """
    # Set up the Turtle Graphics window
    window = turtle.Screen()
    window.title("Turtle Graphics")
    window.setup(width=800, height=600)
    window.bgcolor("white")

    # Create a Turtle object
    turtle = turtle.Turtle()
    turtle.shape("square")
    turtle.color("black")
    turtle.speed(0)

    # Draw the squares
    for i in range(5):
        # Choose a random color from the input list
        color = choice(colors)

        # Draw the square
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.end_fill()

        # Pause for 1 second
        time.sleep(1)

    # Keep the window open
    window.mainloop()
colors = ["red", "green", "blue", "yellow", "purple"]