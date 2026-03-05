
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
    months = list(range(1, 13))
    products = list(sales_data.keys())
    
    fig, ax = plt.subplots()
    
    for product in products:
        sales = sales_data[product]
        mean_sales = statistics.mean(sales)
        std_dev = statistics.stdev(sales)
        
        ax.plot(months, sales, label=product)
        ax.fill_between(months, [mean_sales - std_dev] * len(months), [mean_sales + std_dev] * len(months), alpha=0.3)
    
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends for Five Products')
    ax.legend()
    
    return ax