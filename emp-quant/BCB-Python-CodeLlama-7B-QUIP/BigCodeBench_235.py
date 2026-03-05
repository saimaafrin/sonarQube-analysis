
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    np.random.seed(seed)
    x = np.random.normal(mu, sigma, num_samples)
    hist, bins = np.histogram(x, num_bins)
    pdf = np.cumsum(hist) / num_samples
    pdf_line = plt.plot(bins, pdf, color='red')
    ols_line = ols(x, np.arange(num_bins), color='green')
    plt.show()
    return plt.axes(pdf_line + ols_line)