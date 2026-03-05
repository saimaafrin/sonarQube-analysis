
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    # Generate a dataset with a single feature and a target variable.
    # The target is computed from the feature using a linear relation.
    # In addition, some gaussian noise (random samples from normal distribution),
    # scaled by noise_strength, is added to the target.
    # The dataset is split into training and test sets.
    # Then a linear regression model is adjusted to the training set and the R-squared
    # score is calculated on the test set.

    # Check if test set size is smaller than 2.
    if test_size < 2:
        raise ValueError("Test set size must be greater than 2.")

    # Generate the dataset.
    np.random.seed(random_seed)
    X = np.random.normal(0, 1, size=(num_samples, 1))
    y = np.random.normal(0, 1, size=num_samples) + noise_strength * X

    # Split the dataset into training and test sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Train a linear regression model on the training set.
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate the R-squared score on the test set.
    score = model.score(X_test, y_test)

    return score, model