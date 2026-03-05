
from random import choice
import turtle
import time

def task_func(colors):
    # Set up the Turtle Graphics window
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    # Create a Turtle object
    t = turtle.Turtle()
    t.speed(2)  # Set the drawing speed
    
    # Draw five squares with random colors from the provided list
    for _ in range(5):
        # Choose a random color from the list
        color = choice(colors)
        t.fillcolor(color)
        t.begin_fill()
        
        # Draw a square
        for _ in range(4):
            t.forward(100)
            t.left(90)
        
        t.end_fill()
        t.penup()
        t.goto(choice([-200, 0, 200]), choice([-200, 0, 200]))
        t.pendown()
        
        # Pause for 1 second
        time.sleep(1)
    
    # Keep the window open after drawing
    screen.mainloop()