
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    if test_size < 0.02:
        raise ValueError("Test set size must be at least 2 samples.")
    
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate the dataset
    X = np.random.rand(num_samples, 1)
    y = 2 * X.squeeze() + 1 + noise_strength * np.random.randn(num_samples)
    
    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)
    
    return r_squared, model