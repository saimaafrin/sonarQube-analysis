import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    """
    Generate a dataset with five features sampled from the standard normal distribution and a target variable.
    The target value is created by computing the sum of the features and adding random numbers sampled from the standard normal distribution.
    Then cross-validate the dataset using a RandomForestRegressor model and return the mean cross-validation score.
    """
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv must be greater than or equal to 2")

    # Generate the dataset
    X = np.random.normal(size=(num_samples, 5))
    y = np.sum(X, axis=1) + np.random.normal(size=num_samples)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)

    # Train the model and evaluate its performance
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    scores = cross_val_score(model, X_train, y_train, cv=cv)
    mean_score = np.mean(scores)

    return mean_score, model