import pandas as pd
import numpy as np
def task_func(column, data):
    """
    Analyze a list of sales data, calculate the sum, the mean, the minimum, the maximum of a given column,
    and return the bar chart plot for the given column without displaying it.

    Parameters:
    column (str): The column to analyze. Expected values are ['Product', 'Quantity Sold', 'Total Sales'].
    data (list): The sales data. Expected format: [['Product Name', Quantity Sold (int), Total Sales (int)], ...]
                 The function checks for data validity in the quantity columns (must not be negative).

    Returns:
    tuple: A tuple containing:
        - dict: A dictionary with the sum, mean, min, max of the column.
        - matplotlib.axes.Axes: The Axes object of the plotted bar chart. The bar chart will have Product in its
                                x-axis and the title Bar Chart of (column).

    Requirements:
    - pandas
    - numpy

    Raises:
    - ValueError: If the quantity sold or total sales is negative.
    
    Example:
    >>> data = [['Product A', 100, 10000], ['Product B', 150, 15000], ['Product C', 200, 20000]]
    >>> stats, plot = task_func('Total Sales', data)
    >>> stats
    {'sum': 45000, 'mean': 15000.0, 'min': 10000, 'max': 20000}
    >>> plot
    <Axes: title={'center': 'Bar Chart of Total Sales'}, xlabel='Product'>
    """
    # TODO: Implement the function
    # Hint: Use pandas.DataFrame.from_records() to convert the data to a DataFrame.
    #       Use pandas.DataFrame.sum(), pandas.DataFrame.mean(), pandas.DataFrame.min(), pandas.DataFrame.max()
    #       to calculate the sum, mean, min, max of the column.
    #       Use pandas.DataFrame.plot.bar() to plot the bar chart.
    #       Use matplotlib.pyplot.show() to display the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of the plot.
    #       Use matplotlib.pyplot.xlabel() to set the x-axis label of the plot.
    #       Use matplotlib.pyplot.ylabel() to set the y-axis label of the plot.
    #       Use matplotlib.pyplot.xticks() to set the x-axis ticks of the plot.
    #       Use matplotlib.pyplot.yticks() to set the y-axis ticks of the plot.
    #       Use matplotlib.pyplot.tight_layout() to set the layout of the plot.
    #       Use matplotlib.pyplot.close() to close the plot.
    #       Use matplotlib.pyplot.gca() to get the Axes object of the plotted bar chart.
    #       Use matplotlib.pyplot.title() to set the title of