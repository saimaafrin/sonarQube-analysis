import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading with 'Month' on x-axis and 'Sales' on y-axis.
    """
    # Create a list of sales data for each product
    sales_data = [
        [100, 200, 300, 400, 500],
        [200, 400, 600, 800, 1000],
        [300, 600, 900, 1200, 1500],
        [400, 800, 1200, 1600, 2000],
        [500, 1000, 1500, 2000, 2500]
    ]

    # Create a list of months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the sales data for each product
    for i, product in enumerate(sales_data):
        ax.plot(months, product, label=f'Product {i+1}')

    # Add a legend
    ax.legend()

    # Add a title
    ax.set_title('Sales Trends')

    # Add a label for the y-axis
    ax.set_ylabel('Sales')

    # Add a label for the x-axis
    ax.set_xlabel('Month')

    # Add a shaded region for the standard deviation
    std_dev = statistics.stdev(sales_data)
    ax.fill_between(months, [std_dev] * len(months), color='grey', alpha=0.5)

    # Return the axis object
    return ax
sales_data = [
    [100, 200, 300, 400, 500],
    [200, 400, 600, 800, 1000],
    [300, 600, 900, 1200, 1500],
    [400, 800, 1200, 1600, 2000],
    [500, 1000, 1500, 2000, 2500]
]