import collections
import matplotlib.pyplot as plt
def task_func(data):
    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Iterate over the list of dictionaries
    for d in data:
        # Check if the sales quantity is negative
        if d['sales'] < 0:
            raise ValueError('Sales quantity cannot be negative')

        # Add the sales quantity to the total sales for the fruit
        total_sales[d['fruit']] += d['sales']

    # Create a bar chart of the total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values())

    # Set the colors for each fruit
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    for i, fruit in enumerate(total_sales.keys()):
        ax.patches[i].set_color(colors[i % len(colors)])

    return total_sales, ax
data = [
    {'fruit': 'apple', 'sales': 10},
    {'fruit': 'banana', 'sales': 20},
    {'fruit': 'orange', 'sales': 30},
    {'fruit': 'apple', 'sales': 40},
    {'fruit': 'banana', 'sales': 50},
    {'fruit': 'orange', 'sales': 60},
]