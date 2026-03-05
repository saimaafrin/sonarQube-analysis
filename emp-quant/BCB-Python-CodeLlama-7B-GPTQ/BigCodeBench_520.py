import collections
import matplotlib.pyplot as plt
def task_func(data):
    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Iterate over the list of dictionaries and add the sales quantity for each fruit
    for fruit in data:
        for fruit_name, sales_quantity in fruit.items():
            if sales_quantity < 0:
                raise ValueError("Sales quantity cannot be negative")
            total_sales[fruit_name] += sales_quantity

    # Create a bar chart of total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values())

    # Set the colors for each fruit based on a predefined list
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    for fruit_name, sales_quantity in total_sales.items():
        ax.patches[fruit_name].set_color(colors[fruit_name % len(colors)])

    return total_sales, ax
data = [
    {'apple': 10, 'banana': 20, 'orange': 30},
    {'apple': 20, 'banana': 10, 'orange': 40},
    {'apple': 30, 'banana': 20, 'orange': 50},
]