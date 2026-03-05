
from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(date_str):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the day of the month
    day_of_month = date_obj.day
    
    # Generate a list of random integers with the count equal to the day of the month
    random_integers = [random.randint(1, 100) for _ in range(day_of_month)]
    
    # Create a line plot of the random integers
    fig, ax = plt.subplots()
    ax.plot(random_integers)
    
    # Return the Axes object of the plot
    return ax