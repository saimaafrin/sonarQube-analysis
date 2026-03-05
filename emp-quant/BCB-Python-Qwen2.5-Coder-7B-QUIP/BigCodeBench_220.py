
from random import choice
import turtle
import time
def task_func(colors):
    # Set up the Turtle Graphics window
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Create a Turtle object
    t = turtle.Turtle()
    t.speed(1)  # Set the drawing speed
    
    # Draw five squares of random colors
    for _ in range(5):
        # Choose a random color from the list
        color = choice(colors)
        t.color(color)
        
        # Draw a square
        for _ in range(4):
            t.forward(100)
            t.right(90)
        
        # Pause for 1 second
        time.sleep(1)
    
    # Close the window after drawing
    window.mainloop()