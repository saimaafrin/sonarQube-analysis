
from random import choice
import turtle
import time

def task_func(colors):
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Random Squares")
    
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(2)  # Adjust speed if needed
    
    for _ in range(5):
        # Choose a random color from the list
        color = choice(colors)
        t.fillcolor(color)
        
        # Start filling the shape
        t.begin_fill()
        
        # Draw a square
        for _ in range(4):
            t.forward(100)
            t.left(90)
        
        # End filling the shape
        t.end_fill()
        
        # Pause for 1 second
        time.sleep(1)
    
    # Hide the turtle
    t.hideturtle()
    
    # Keep the window open until it's closed manually
    screen.mainloop()