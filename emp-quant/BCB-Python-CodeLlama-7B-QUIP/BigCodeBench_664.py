
import statistics
import matplotlib.pyplot as plt

def task_func(sales_data):
    # Calculate the mean and standard deviation of the sales data
    mean = statistics.mean(sales_data)
    std_dev = statistics.stdev(sales_data)

    # Create a figure and axes objects
    fig, ax = plt.subplots()

    # Plot the sales trends
    ax.plot(sales_data, label='Sales')

    # Add standard deviation shading
    ax.fill_between(sales_data, mean - std_dev, mean + std_dev, facecolor='gray', alpha=0.25, label='Standard Deviation')

    # Set the x-axis and y-axis labels
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')

    # Set the figure title
    ax.set_title('Sales Trends')

    # Return the axes object
    return ax