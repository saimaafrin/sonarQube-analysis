
from scipy import stats
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Calculate the correlation coefficient
    correlation_coefficient = stats.pearsonr(data_dict[data_keys[0]], data_dict[data_keys[1]])[0]

    # Plot the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data_dict[data_keys[0]], data_dict[data_keys[1]], label=f'Correlation Coefficient: {correlation_coefficient}')
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Correlation Plot for {data_keys[0]} and {data_keys[1]}')
    ax.legend()
    plt.show()

    return correlation_coefficient, fig