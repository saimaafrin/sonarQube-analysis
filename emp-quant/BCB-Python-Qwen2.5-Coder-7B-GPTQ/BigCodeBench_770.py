import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    """
    Generates a dataset, trains a linear regression model, and returns the R-squared score and the model.
    
    Parameters:
    - num_samples (int): The number of samples in the dataset.
    - noise_strength (float): The standard deviation of the Gaussian noise added to the target.
    - random_seed (int): Seed for the random number generator for reproducibility.
    - test_size (float): The proportion of the dataset to include in the test split.
    
    Returns:
    - float: The R-squared score of the fitted model on the test set.
    - LinearRegression: The trained linear regression model.
    """
    if test_size < 0.02:
        raise ValueError("Test set size must be at least 2 samples.")
    
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate the dataset
    X = np.random.rand(num_samples, 1)
    y = 2 * X.squeeze() + 1  # Linear relation: y = 2x + 1
    y += noise_strength * np.random.randn(num_samples)  # Add Gaussian noise
    
    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)
    
    return r_squared, model