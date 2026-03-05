import collections
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        return {}, None

    total_sales = collections.defaultdict(int)
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    color_map = {}

    for item in data:
        fruit = item['fruit']
        quantity = item['quantity']
        price = item['price']

        if quantity < 0:
            raise ValueError("Sales quantity must not be negative")

        total_sales[fruit] += quantity * price

        if fruit not in color_map:
            color_map[fruit] = colors.pop(0)

    fig, ax = plt.subplots()
    ax.bar(total_sales.keys(), total_sales.values(), color=[color_map[fruit] for fruit in total_sales])

    return dict(total_sales), ax