import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading with 'Month' on x-axis and 'Sales' on y-axis.
    """
    # Create a list of sales data for each product
    sales_data_list = [sales_data[0], sales_data[1], sales_data[2], sales_data[3], sales_data[4]]

    # Create a list of months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Create a list of sales for each month
    sales_by_month = [sales_data_list[0][0], sales_data_list[1][0], sales_data_list[2][0], sales_data_list[3][0], sales_data_list[4][0]]

    # Create a list of standard deviations for each month
    std_devs = [statistics.stdev(sales_data_list[0]), statistics.stdev(sales_data_list[1]), statistics.stdev(sales_data_list[2]), statistics.stdev(sales_data_list[3]), statistics.stdev(sales_data_list[4])]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the sales trends for each product
    for i in range(len(sales_data_list)):
        ax.plot(months, sales_data_list[i], label=f'Product {i+1}')

    # Shade the standard deviation for each month
    for i in range(len(std_devs)):
        ax.fill_between(months, sales_by_month[i] - std_devs[i], sales_by_month[i] + std_devs[i], alpha=0.2, label=f'Standard Deviation {i+1}')

    # Set the x-axis label and y-axis label
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')

    # Set the title of the plot
    ax.set_title('Sales Trends for Five Products')

    # Add a legend to the plot
    ax.legend()

    # Return the axes object
    return ax
sales_data = [[100, 120, 130, 140, 150], [110, 125, 135, 145, 155], [120, 130, 140, 150, 160], [130, 140, 150, 160, 170], [140, 150, 160, 170, 180]]