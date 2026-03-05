import collections
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        return {}, None

    total_sales = collections.defaultdict(int)
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    color_index = 0

    for entry in data:
        fruit = entry['fruit']
        quantity = entry['quantity']
        price = entry['price']

        if quantity < 0:
            raise ValueError("Sales quantity cannot be negative")

        total_sales[fruit] += quantity * price

    if not total_sales:
        return {}, None

    fruits = list(total_sales.keys())
    sales = [total_sales[fruit] for fruit in fruits]
    color_cycle = colors[:len(fruits)]

    fig, ax = plt.subplots()
    ax.bar(fruits, sales, color=color_cycle)

    return total_sales, ax