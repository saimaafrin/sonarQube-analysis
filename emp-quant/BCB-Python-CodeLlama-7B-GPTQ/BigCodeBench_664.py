import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading with 'Month' on x-axis and 'Sales' on y-axis.
    """
    # Create a list of sales data for each product
    sales_data = [
        [100, 120, 150, 180, 200],
        [120, 140, 160, 180, 200],
        [150, 180, 210, 240, 270],
        [180, 210, 240, 270, 300],
        [200, 230, 260, 290, 320]
    ]

    # Calculate the mean and standard deviation for each product
    means = [statistics.mean(sales) for sales in sales_data]
    stds = [statistics.stdev(sales) for sales in sales_data]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the sales trends for each product
    for i, sales in enumerate(sales_data):
        ax.plot(sales, label=f"Product {i+1}")

    # Add a legend to the plot
    ax.legend()

    # Add a shaded area for the standard deviation
    for i, mean in enumerate(means):
        std = stds[i]
        ax.fill_between(sales, [mean - std, mean + std], alpha=0.2, label=f"Product {i+1} standard deviation")

    # Set the x-axis label and y-axis label
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")

    # Return the axis object
    return ax
sales_data = [
    [100, 120, 150, 180, 200],
    [120, 140, 160, 180, 200],
    [150, 180, 210, 240, 270],
    [180, 210, 240, 270, 300],
    [200, 230, 260, 290, 320]
]