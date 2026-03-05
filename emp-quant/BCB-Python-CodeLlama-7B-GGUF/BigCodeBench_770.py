
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    # Generate a dataset with a single feature and a target variable
    X = np.random.normal(size=num_samples)
    y = 2 * X + np.random.normal(scale=noise_strength, size=num_samples)

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)

    # Create a linear regression model and fit it to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate the R-squared score of the fitted model on the test set
    y_pred = model.predict(X_test)
    r2 = model.score(X_test, y_test)

    # Raise an exception if the test set size is smaller than 2
    if len(X_test) < 2:
        raise ValueError("Test set size is smaller than 2")

    return r2, model