
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(date_str):
    # Parse the date string to get the day of the month
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_month = date.day
    
    # Generate a list of random integers equal to the day of the month
    random_integers = [random.randint(1, 100) for _ in range(day_of_month)]
    
    # Create a line plot of the random integers
    fig, ax = plt.subplots()
    ax.plot(random_integers)
    
    # Return the Axes object of the plot
    return ax