
import statistics
import matplotlib.pyplot as plt

def task_func(sales_data):
    # Calculate the standard deviation of sales for each month
    std_devs = [statistics.stdev(sales_data[i]) for i in range(len(sales_data))]

    # Create a bar plot with the standard deviation shading
    fig, ax = plt.subplots()
    ax.bar(range(len(sales_data)), sales_data, yerr=std_devs)
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Sales Trends')
    ax.set_xticks(range(len(sales_data)))
    ax.set_xticklabels(sales_data.index)
    ax.set_ylim(0, max(sales_data) * 1.1)
    ax.grid(True)

    return ax