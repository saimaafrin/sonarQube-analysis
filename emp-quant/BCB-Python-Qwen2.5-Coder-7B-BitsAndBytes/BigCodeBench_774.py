
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    if num_samples // cv < 2:
        raise ValueError("num_samples / cv must be at least 2")
    
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate the dataset
    X = np.random.randn(num_samples, 5)
    y = np.sum(X, axis=1) + np.random.randn(num_samples)
    
    # Initialize the RandomForestRegressor
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    
    # Perform cross-validation
    scores = cross_val_score(model, X, y, cv=cv)
    
    # Return the mean cross-validation score and the trained model
    return scores.mean(), model