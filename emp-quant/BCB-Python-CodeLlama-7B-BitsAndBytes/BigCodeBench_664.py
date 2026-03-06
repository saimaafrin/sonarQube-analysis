
import statistics
import matplotlib.pyplot as plt

def task_func(sales_data):
    # Calculate the mean and standard deviation of the sales data
    mean = statistics.mean(sales_data)
    stddev = statistics.stdev(sales_data)

    # Create a figure and axes object
    fig, ax = plt.subplots()

    # Plot the sales trends
    ax.plot(sales_data, label='Sales')

    # Shade the area between the mean and the standard deviation
    ax.fill_between(sales_data, mean - stddev, mean + stddev, alpha=0.5, label='Standard Deviation')

    # Set the x-axis label and y-axis label
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')

    # Add a legend
    ax.legend()

    # Return the axes object
    return ax