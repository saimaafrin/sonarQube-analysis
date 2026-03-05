
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, num_samples)
    bins = np.linspace(x.min(), x.max(), num_bins)
    hist, bin_edges = np.histogram(x, bins=bins)
    pdf = np.exp(-(bin_edges[:-1] - mu)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align='edge', alpha=0.5)
    plt.plot(bin_edges[:-1], pdf, color='red')
    x_fit = np.linspace(bin_edges[0], bin_edges[-1], num_samples)
    y_fit = np.poly1d(ols(x_fit, np.log(hist)).params)
    plt.plot(x_fit, np.exp(y_fit), color='green')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normal Distribution with PDF and OLS Fit')
    return plt.gca()