
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Check if data is empty
    if not data:
        return {}, None
    
    # Initialize a defaultdict to store total sales
    total_sales = collections.defaultdict(int)
    
    # Iterate over each dictionary in the list
    for item in data:
        # Ensure sales quantity is non-negative
        if item['sales'] < 0:
            raise ValueError("Sales quantity cannot be negative")
        
        # Add sales to the total sales for the corresponding fruit
        total_sales[item['fruit']] += item['sales']
    
    # Prepare data for plotting
    fruits = list(total_sales.keys())
    sales = list(total_sales.values())
    colors = ['red', 'yellow', 'green', 'blue', 'purple'][:len(fruits)]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(fruits, sales, color=colors)
    
    # Set labels and title
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Total Sales')
    ax.set_title('Total Fruit Sales')
    
    # Return the total sales dictionary and the bar chart axes
    return dict(total_sales), ax