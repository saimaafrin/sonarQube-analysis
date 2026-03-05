
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    if cv < 2:
        raise ValueError("num_samples / cv < 2")

    # Generate the dataset
    features = np.random.normal(size=num_samples)
    target = np.sum(features) + np.random.normal(size=num_samples)

    # Split the dataset into training and testing sets
    train_features = features[:int(num_samples * 0.8)]
    train_target = target[:int(num_samples * 0.8)]
    test_features = features[int(num_samples * 0.8):]
    test_target = target[int(num_samples * 0.8):]

    # Train the model
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    model.fit(train_features, train_target)

    # Evaluate the model on the testing set
    results = cross_val_score(model, test_features, test_target)

    return results, model