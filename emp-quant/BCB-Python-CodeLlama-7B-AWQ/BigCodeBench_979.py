import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    """
    Shuffle the columns of a given numpy array and train a Random Forest Classifier on the shuffled data.

    Args:
        feature_array (numpy array): The feature data to be shuffled and used for training.
        target_array (numpy array): The target data to be used for training.
        feature_names (list of str, optional): The names of the features in the feature array. Defaults to ["f1", "f2", "f3", "f4", "f5"].
        target_name (str, optional): The name of the target variable. Defaults to "target".
        seed (int, optional): The random seed to use for shuffling the columns. Defaults to None.

    Returns:
        sklearn.ensemble.RandomForestClassifier: A trained Random Forest Classifier on the shuffled feature data.
    """
    # Shuffle the columns of the feature array
    if seed is not None:
        np.random.seed(seed)
    feature_array = np.random.permutation(feature_array)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(feature_array, target_array, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier on the shuffled data
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate the model on the testing data
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")

    return clf
feature_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
target_array = np.array([0, 1, 1])