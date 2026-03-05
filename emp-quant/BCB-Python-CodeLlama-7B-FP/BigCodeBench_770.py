import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    """
    Generate a dataset with a single feature and a target variable. The target is computed from the feature using a linear relation. In addition some gaussian noise (random samples from normal distribution), scaled by noise_strength, is added to the target. The dataset is split into training and test sets. Then a linear regression model is adjusted to the training set and the R-squared score is calculated on the test set.
    The function should raise the exception for: ValueError: If test set size is smaller than 2.
    The function should output with:
        float: The R-squared score of the fitted model on the test set.
        LinearRegression: The trained linear regression model.
    """
    # Generate a random feature vector
    X = np.random.rand(num_samples, 1)

    # Generate a target vector using a linear relation
    y = 2 * X + 3

    # Add gaussian noise to the target vector
    y += np.random.normal(scale=noise_strength, size=num_samples)

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_seed)

    # Train a linear regression model on the training set
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate the R-squared score on the test set
    y_pred = model.predict(X_test)
    r2 = model.score(X_test, y_test)

    # Check if the test set size is smaller than 2
    if test_size < 2:
        raise ValueError("Test set size is smaller than 2")

    # Return the R-squared score and the trained linear regression model
    return r2, model