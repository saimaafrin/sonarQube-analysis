import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.formula.api import ols
def task_func(mu, sigma, seed=0, num_samples=1000, num_bins=30):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)
    
    # Create a histogram of the samples
    fig, ax = plt.subplots()
    ax.hist(samples, bins=num_bins, density=True, alpha=0.6, color='g')
    
    # Calculate the range of the histogram
    x_min, x_max = ax.get_xlim()
    
    # Generate x values for the PDF and OLS lines
    x = np.linspace(x_min, x_max, 100)
    
    # Calculate the PDF of the normal distribution
    pdf = norm.pdf(x, mu, sigma)
    
    # Overlay the PDF on the histogram
    ax.plot(x, pdf, 'r-', lw=2)
    
    # Fit a second order polynomial using OLS regression
    # Convert x to a DataFrame and add a constant term
    x_df = pd.DataFrame({'x': x, 'x2': x**2})
    x_df['const'] = 1
    
    # Fit the OLS model
    model = ols('y ~ x + x2', data={'y': pdf}).fit()
    
    # Predict the y values using the fitted model
    y_ols = model.predict(x_df)
    
    # Overlay the OLS line on the histogram
    ax.plot(x, y_ols, 'g-', lw=2)
    
    # Return the Axes object
    return ax