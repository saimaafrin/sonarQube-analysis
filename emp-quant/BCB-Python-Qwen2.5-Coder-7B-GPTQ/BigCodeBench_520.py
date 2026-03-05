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
        sales = entry['sales']
        turnover = entry['turnover']

        if sales < 0:
            raise ValueError("Sales quantity must not be negative")

        total_sales[fruit] += sales

        if color_index >= len(colors):
            color_index = 0

    fig, ax = plt.subplots()
    ax.bar(total_sales.keys(), total_sales.values(), color=[colors[color_index]])
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Fruit Sales')

    return total_sales, ax