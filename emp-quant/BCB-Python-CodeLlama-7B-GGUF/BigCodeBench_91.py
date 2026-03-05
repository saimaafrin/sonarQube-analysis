
from scipy.stats import linregress
import matplotlib.pyplot as plt

def task_func(data, column1, column2):
    if column1 not in data.columns or column2 not in data.columns:
        raise ValueError("Specified columns do not exist in the DataFrame")

    slope, intercept, r_value, p_value, std_err = linregress(data[column1], data[column2])

    fig, ax = plt.subplots()
    ax.plot(data[column1], data[column2], 'bo')
    ax.plot(data[column1], intercept + slope * data[column1], 'r')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.set_title("Linear Regression")

    return (slope, intercept, r_value, p_value, std_err), ax