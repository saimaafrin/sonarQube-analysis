import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading.

    Parameters:
    sales_data (dict): A dictionary where keys are product names and values are lists of sales data for each month.

    Returns:
    ax (matplotlib.axes.Axes): Axes object with the sales trends plot.
    """
    # Extracting data for plotting
    months = list(range(1, 13))
    product_names = list(sales_data.keys())
    mean_sales = [statistics.mean(sales_data[product]) for product in product_names]
    std_dev_sales = [statistics.stdev(sales_data[product]) for product in product_names]

    # Creating the plot
    fig, ax = plt.subplots()
    for product, mean, std_dev in zip(product_names, mean_sales, std_dev_sales):
        ax.fill_between(months, [mean - std_dev] * 12, [mean + std_dev] * 12, alpha=0.3, label=f'{product} ± std dev')
        ax.plot(months, [mean] * 12, label=product)

    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends for Five Products Over a Year')
    ax.legend()
    plt.show()

    return ax