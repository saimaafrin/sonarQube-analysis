
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Create a dictionary to store the total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Loop through the list of dictionaries and add the sales quantity for each fruit
    for d in data:
        for k, v in d.items():
            if k in total_sales:
                total_sales[k] += v
            else:
                total_sales[k] = v

    # Check for negative sales quantities and throw a ValueError if encountered
    for k, v in total_sales.items():
        if v < 0:
            raise ValueError(f"Negative sales quantity for {k}: {v}")

    # Create a bar chart of the total fruit sales
    ax = plt.bar(total_sales.keys(), total_sales.values(), color=['red', 'yellow', 'green', 'blue', 'purple'])

    return total_sales, ax