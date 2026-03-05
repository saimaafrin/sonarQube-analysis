
from random import choice
import turtle
import time

def task_func(colors):
    # Set up the Turtle Graphics window
    screen = turtle.Screen()
    screen.title("Random Colored Squares")
    screen.bgcolor("white")

    # Create a Turtle object
    t = turtle.Turtle()
    t.speed(2)  # Set the drawing speed

    # Draw five squares with random colors
    for _ in range(5):
        # Choose a random color from the list
        color = choice(colors)
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
        t.penup()
        t.forward(120)  # Move to the next position
        t.pendown()
        time.sleep(1)  # Pause for 1 second

    # Keep the window open after drawing
    screen.mainloop()