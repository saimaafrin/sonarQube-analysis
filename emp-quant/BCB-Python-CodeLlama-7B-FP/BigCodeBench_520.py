import collections
import matplotlib.pyplot as plt
def task_func(data):
    """
    Combine a list of dictionaries with the same keys (fruit names) into a single dictionary, calculate the total turnover for each fruit, and return a bar chart's axes with colors representing different fruits. The colors are selected from: 'red', 'yellow', 'green', 'blue', 'purple'. The function ensures that sales quantity must not be negative, throwing a ValueError if encountered.
    """
    # Check if data is empty
    if not data:
        return None, None

    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Iterate over the data and calculate the total turnover for each fruit
    for fruit in data:
        for key, value in fruit.items():
            if value < 0:
                raise ValueError("Sales quantity must not be negative")
            total_sales[key] += value

    # Create a bar chart of total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values(), color=['red', 'yellow', 'green', 'blue', 'purple'])

    return total_sales, ax
data = [
    {'apple': 10, 'banana': 20, 'orange': 30},
    {'apple': 40, 'banana': 50, 'orange': 60},
    {'apple': 70, 'banana': 80, 'orange': 90}
]