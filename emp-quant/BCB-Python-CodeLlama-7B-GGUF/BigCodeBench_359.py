
from scipy import stats
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Calculate the correlation between the two data series
    corr_coef = stats.pearsonr(data_dict[data_keys[0]], data_dict[data_keys[1]])[0]

    # Create a scatter plot of the two data series
    fig, ax = plt.subplots()
    ax.scatter(data_dict[data_keys[0]], data_dict[data_keys[1]])
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Correlation Coefficient: {corr_coef:.2f}')

    return corr_coef, ax

corr_coef, ax = task_func(data_dict, data_keys)
print(corr_coef)
ax.show()