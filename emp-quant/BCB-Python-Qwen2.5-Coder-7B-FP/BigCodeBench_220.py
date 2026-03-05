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
    
    # Function to draw a square with a given color
    def draw_square(color):
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
    
    # Draw five squares with random colors from the list
    for _ in range(5):
        color = choice(colors)
        draw_square(color)
        time.sleep(1)  # Pause for 1 second between squares
    
    # Keep the window open after drawing
    screen.mainloop()
colors = ["red", "blue", "green", "yellow", "purple"]