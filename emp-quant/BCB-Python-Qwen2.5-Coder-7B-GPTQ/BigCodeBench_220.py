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
    
    # Loop through each color in the list
    for color in colors:
        # Set the pen color
        t.color(color)
        
        # Draw a square
        for _ in range(4):
            t.forward(100)  # Draw a side of the square
            t.right(90)    # Turn right by 90 degrees
        
        # Pause for 1 second
        time.sleep(1)
    
    # Close the Turtle Graphics window
    screen.mainloop()
colors = ["red", "blue", "green", "yellow", "purple"]