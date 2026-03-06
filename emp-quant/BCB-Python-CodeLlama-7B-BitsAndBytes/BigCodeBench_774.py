
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    # Generate a dataset with five features sampled from the standard normal distribution and a target variable
    X = np.random.randn(num_samples, 5)
    y = X.sum(axis=1) + np.random.randn(num_samples)

    # Create a RandomForestRegressor model with the specified number of estimators
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)

    # Cross-validate the model using the specified number of folds
    scores = cross_val_score(model, X, y, cv=cv)

    # Return the mean cross-validation score and the trained model
    return np.mean(scores), model