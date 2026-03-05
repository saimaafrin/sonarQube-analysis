
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Check if data is empty
    if not data:
        return {}, None

    # Initialize a dictionary to hold total sales for each fruit
    total_sales = collections.defaultdict(int)

    # Process each item in the data
    for item in data:
        # Ensure sales quantity is not negative
        if item['sales'] < 0:
            raise ValueError("Sales quantity cannot be negative")

        # Add the sales to the total sales for the corresponding fruit
        total_sales[item['fruit']] += item['sales']

    # Prepare data for the bar chart
    fruits = list(total_sales.keys())
    sales = list(total_sales.values())

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(fruits, sales, color='blue')

    # Set the color for each bar based on the fruit
    colors = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange', 'grape': 'green', 'berry': 'purple'}
    ax.bar(fruits, sales, color=[colors[fruit] for fruit in fruits])

    # Set the labels and title
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Fruit Sales')

    # Return the total sales and the bar chart
    return total_sales, ax