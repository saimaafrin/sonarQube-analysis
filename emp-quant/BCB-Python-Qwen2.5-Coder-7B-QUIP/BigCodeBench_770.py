
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.exceptions import ValueError

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    # Set a random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)

    # Generate a single feature
    X = np.random.rand(num_samples, 1)

    # Generate the target variable using a linear relation
    true_slope = 2
    true_intercept = 1
    y = true_slope * X + true_intercept

    # Add gaussian noise to the target
    noise = np.random.randn(num_samples, 1) * noise_strength
    y += noise

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Check if the test set size is smaller than 2
    if len(y_test) < 2:
        raise ValueError("Test set size is smaller than 2")

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate the R-squared score on the test set
    r_squared = model.score(X_test, y_test)

    return r_squared, model