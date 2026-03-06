
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    if test_size < 2:
        raise ValueError("Test set size must be at least 2.")
    
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate the data
    X = np.random.rand(num_samples, 1) * 10
    y = 3 * X.squeeze() + 2 + noise_strength * np.random.randn(num_samples)
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    
    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)
    
    return r_squared, model