
import statistics
import matplotlib.pyplot as plt

def task_func(sales_data):
    """
    Plots sales trends for five products over a year, highlighting variability with standard deviation shading.
    
    Parameters:
    sales_data (dict): A dictionary where keys are product names and values are lists of monthly sales data.
    
    Returns:
    ax (matplotlib.axes.Axes): Axes object with the sales trends plot.
    """
    # Extracting data
    months = list(range(1, 13))
    products = list(sales_data.keys())
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plotting each product's sales with standard deviation shading
    for product in products:
        sales = sales_data[product]
        mean_sales = statistics.mean(sales)
        std_dev = statistics.stdev(sales)
        
        # Plot the mean sales line
        ax.plot(months, [mean_sales] * len(months), label=product)
        
        # Fill the area between mean - std_dev and mean + std_dev
        ax.fill_between(months, [mean_sales - std_dev] * len(months), [mean_sales + std_dev] * len(months), alpha=0.2)
    
    # Setting labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends for Five Products Over a Year')
    ax.legend()
    
    return ax

ax = task_func(sales_data)
plt.show()