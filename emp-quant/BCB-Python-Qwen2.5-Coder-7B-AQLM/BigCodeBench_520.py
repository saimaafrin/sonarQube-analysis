
import collections
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        return {}, None

    total_sales = collections.defaultdict(int)
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    color_index = 0

    for fruit_data in data:
        for fruit, sales in fruit_data.items():
            if sales < 0:
                raise ValueError("Sales quantity cannot be negative")
            total_sales[fruit] += sales

    if not total_sales:
        return {}, None

    fruits = list(total_sales.keys())
    sales = list(total_sales.values())

    fig, ax = plt.subplots()
    ax.bar(fruits, sales, color=[colors[i % len(colors)] for i in range(len(fruits))])

    ax.set_xlabel('Fruit')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Fruit Sales')

    return total_sales, ax