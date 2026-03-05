
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Check if data is empty
    if not data:
        return None, None

    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Iterate over the data and calculate the total turnover for each fruit
    for fruit, quantity in data:
        if quantity < 0:
            raise ValueError("Sales quantity cannot be negative")
        total_sales[fruit] += quantity

    # Create a bar chart of total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values())

    # Set the colors for each fruit based on a predefined list
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    for fruit, color in zip(total_sales.keys(), colors):
        ax.patches[fruit].set_color(color)

    return total_sales, ax