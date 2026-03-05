
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.exceptions import ValueError

def task_func(num_samples=100, n_estimators=100, random_seed=None, cv=5):
    # Generate the dataset
    np.random.seed(random_seed)
    features = np.random.randn(num_samples, 5)
    target = np.sum(features, axis=1) + np.random.randn(num_samples)
    
    # Check if num_samples / cv < 2
    if num_samples / cv < 2:
        raise ValueError("num_samples / cv must be at least 2")
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=random_seed)
    
    # Initialize and train the RandomForestRegressor
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_seed)
    model.fit(X_train, y_train)
    
    # Perform cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='neg_mean_squared_error')
    
    # Return the mean cross-validation score
    mean_score = np.mean(np.abs(scores))
    
    return mean_score, model