
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Iterate over the list of dictionaries and calculate the total sales for each fruit
    for d in data:
        for fruit, quantity in d.items():
            if quantity < 0:
                raise ValueError("Sales quantity cannot be negative")
            total_sales[fruit] += quantity

    # Create a bar chart of the total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values())

    # Set the colors of the bars based on the fruit names
    for i, fruit in enumerate(total_sales.keys()):
        if fruit == "apple":
            ax.patches[i].set_color("red")
        elif fruit == "banana":
            ax.patches[i].set_color("yellow")
        elif fruit == "orange":
            ax.patches[i].set_color("green")
        elif fruit == "mango":
            ax.patches[i].set_color("blue")
        else:
            ax.patches[i].set_color("purple")

    return total_sales, ax

total_sales, ax = task_func(data)
print(total_sales)
ax.show()