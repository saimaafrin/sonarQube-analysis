
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv must be greater than or equal to 2")

    # Generate random features and target variable
    features = np.random.normal(size=(num_samples, 5))
    target = np.sum(features, axis=1) + np.random.normal(size=num_samples)

    # Create and train the model
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    model.fit(features, target)

    # Evaluate the model using cross-validation
    scores = cross_val_score(model, features, target, cv=cv)

    # Return the mean cross-validation score and the trained model
    return np.mean(scores), model

results = task_func(random_seed=1)
print(results)