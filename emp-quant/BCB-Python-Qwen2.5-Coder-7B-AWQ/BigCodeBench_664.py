import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading.

    Parameters:
    sales_data (dict): A dictionary where keys are product names and values are lists of sales figures for each month.

    Returns:
    ax (matplotlib.axes.Axes): Axes object with the sales trends plot.
    """
    months = list(range(1, 13))
    products = list(sales_data.keys())
    colors = plt.cm.viridis(np.linspace(0, 1, len(products)))

    fig, ax = plt.subplots()

    for product, sales in zip(products, sales_data.values()):
        mean_sales = [statistics.mean(sales[:i+1]) for i in range(len(sales))]
        std_sales = [statistics.stdev(sales[:i+1]) for i in range(len(sales))]
        ax.fill_between(months, [m - s for m, s in zip(mean_sales, std_sales)], [m + s for m, s in zip(mean_sales, std_sales)], color=colors[products.index(product)], alpha=0.3)
        ax.plot(months, mean_sales, label=product, color=colors[products.index(product)])

    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends for Five Products Over a Year')
    ax.legend()
    plt.show()

    return ax