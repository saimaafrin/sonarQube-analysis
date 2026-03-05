import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    """
    Shuffles the columns of a given numpy array and trains a Random Forest Classifier on the shuffled data.

    Parameters:
    - feature_array: numpy array, the feature data.
    - target_array: numpy array, the target data.
    - feature_names: list of str, the names of the feature columns.
    - target_name: str, the name of the target column.
    - seed: int, the seed for the random number generator for reproducibility.

    Returns:
    - sklearn.ensemble.RandomForestClassifier: A trained Random Forest Classifier on the shuffled feature data.
    """
    # Ensure the input arrays are numpy arrays
    feature_array = np.array(feature_array)
    target_array = np.array(target_array)

    # Shuffle the columns of the feature array
    if seed is not None:
        np.random.seed(seed)
    shuffled_indices = np.random.permutation(feature_array.shape[1])
    shuffled_feature_array = feature_array[:, shuffled_indices]

    # Create a DataFrame for the shuffled feature array and target array
    shuffled_df = pd.DataFrame(shuffled_feature_array, columns=feature_names)
    shuffled_df[target_name] = target_array

    # Train a Random Forest Classifier
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(shuffled_df[feature_names], shuffled_df[target_name])

    return rf_classifier